import random
from datetime import timedelta
from faker import Faker
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

# Imports for the models based on the schema
from apps.accounts.models import User, StudentProfile, TeacherProfile
from apps.schools.models import School, AcademicYear, Subject, Classroom, ClassroomEnrollment
from apps.lectures.models import Lecture
from apps.notes.models import LectureNote
from apps.assignments.models import Assignment, AssignmentSubmission, AssignmentGrade
from apps.gamification.models import StudentXP, XPTransaction, Leaderboard, LeaderboardEntry

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with realistic dummy data chronologically'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting data generation...'))
        
        # Step 1: Base Organization
        school, _ = School.objects.get_or_create(
            code="SCH001",
            defaults={
                "name": "Springfield Elementary",
                "city": "Springfield",
                "state": "IL",
                "principal_name": "Seymour Skinner",
                "established_year": 1990
            }
        )
        self.stdout.write('Step 1: Created School')
        
        today = timezone.now().date()
        academic_year, _ = AcademicYear.objects.get_or_create(
            school=school,
            name=f"{today.year}-{today.year+1}",
            defaults={
                "start_date": today.replace(month=8, day=1),
                "end_date": today.replace(year=today.year+1, month=6, day=30),
                "is_current": True
            }
        )
        self.stdout.write('Step 1: Created Academic Year')

        # Step 2: Users & Profiles
        students = []
        for i in range(20):
            email = f"student{i+1}@example.com"
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "role": "student"
                }
            )
            if created:
                user.set_password("password123")
                user.save()
            
            StudentProfile.objects.get_or_create(
                user=user,
                defaults={"grade": random.randint(1, 5)}
            )
            students.append(user)
        self.stdout.write('Step 2: Created 20 Students')

        teachers = []
        for i in range(5):
            email = f"teacher{i+1}@example.com"
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "role": "teacher"
                }
            )
            if created:
                user.set_password("password123")
                user.save()
                
            TeacherProfile.objects.get_or_create(
                user=user,
                defaults={"employee_id": f"TCH{i+1:03d}", "specialization": fake.job()}
            )
            teachers.append(user)
        self.stdout.write('Step 2: Created 5 Teachers')

        # Step 3: Subjects
        subject_names = ["Mathematics", "Science", "English", "History", "Art"]
        subjects = []
        for name in subject_names:
            subject, _ = Subject.objects.get_or_create(
                code=name[:3].upper(),
                defaults={
                    "name": name,
                    "description": fake.sentence(),
                    "grade": 5
                }
            )
            subjects.append(subject)
        self.stdout.write('Step 3: Created Subjects')

        # Step 4: Classrooms & Teacher Assignments
        # Teacher 1 gets two subjects
        class_a, _ = Classroom.objects.get_or_create(
            class_code="CLASS-A",
            defaults={
                "school": school,
                "academic_year": academic_year,
                "subject": subjects[0],  # Math
                "grade": 5,
                "section": "A",
                "teacher": teachers[0],  # Teacher 1
                "room_number": "101"
            }
        )
        
        class_b, _ = Classroom.objects.get_or_create(
            class_code="CLASS-B",
            defaults={
                "school": school,
                "academic_year": academic_year,
                "subject": subjects[1],  # Science
                "grade": 5,
                "section": "B",
                "teacher": teachers[0],  # Teacher 1
                "room_number": "102"
            }
        )
        
        # We need a total of exactly 3 subjects per teacher, but classroom links to 1 subject and 1 teacher.
        # So we create more classrooms to satisfy the "3 subjects per teacher" requirement via classroom assignments
        # Teacher 1 (already has 2 subjects from Class A & B) -> Needs 1 more
        Classroom.objects.get_or_create(class_code="T1-EXTRA1", defaults={"school": school, "academic_year": academic_year, "subject": subjects[2], "grade": 5, "section": "Extra", "teacher": teachers[0], "room_number": "103"})
        
        # Teachers 2 & 3: Assign to Class A's room/section technically, but each needs 3 subjects
        for t_idx, teacher in enumerate([teachers[1], teachers[2]]):
            for s_idx in range(3):
                Classroom.objects.get_or_create(
                    class_code=f"T{t_idx+2}-SUB{s_idx}",
                    defaults={
                        "school": school, "academic_year": academic_year,
                        "subject": subjects[s_idx], "grade": 5, "section": f"A-{t_idx+2}-{s_idx}",
                        "teacher": teacher, "room_number": f"20{t_idx}"
                    }
                )
                
        # Teachers 4 & 5: Assign to Class B's section, 3 subjects each
        for t_idx, teacher in enumerate([teachers[3], teachers[4]]):
            for s_idx in range(3):
                Classroom.objects.get_or_create(
                    class_code=f"T{t_idx+4}-SUB{s_idx}",
                    defaults={
                        "school": school, "academic_year": academic_year,
                        "subject": subjects[s_idx], "grade": 5, "section": f"B-{t_idx+4}-{s_idx}",
                        "teacher": teacher, "room_number": f"30{t_idx}"
                    }
                )
        self.stdout.write('Step 4: Created Classrooms & Teacher Assignments')

        # Step 5: Student Enrollments
        class_a_students = students[:10]
        class_b_students = students[10:]
        
        for student in class_a_students:
            ClassroomEnrollment.objects.get_or_create(classroom=class_a, student=student, defaults={"enrollment_date": today})
            
        for student in class_b_students:
            ClassroomEnrollment.objects.get_or_create(classroom=class_b, student=student, defaults={"enrollment_date": today})
        self.stdout.write('Step 5: Created Enrollments')

        # Step 6: Core Content (Lectures & Notes)
        for classroom in [class_a, class_b]:
            for i in range(3):
                lecture, _ = Lecture.objects.get_or_create(
                    classroom=classroom,
                    title=f"Lecture {i+1} for {classroom.class_code}",
                    defaults={
                        "teacher": classroom.teacher,
                        "description": fake.paragraph(),
                        "chapter": f"Chapter {i+1}",
                        "topic": fake.word(),
                        "status": "published",
                        "is_shared_with_students": True,
                        "shared_at": timezone.now()
                    }
                )
                
                LectureNote.objects.get_or_create(
                    lecture=lecture,
                    defaults={
                        "classroom": classroom,
                        "teacher": classroom.teacher,
                        "title": f"Notes for {lecture.title}",
                        "content": fake.text(),
                        "summary": fake.sentence(),
                        "is_published": True,
                        "published_at": timezone.now(),
                        "is_auto_generated": False
                    }
                )
        self.stdout.write('Step 6: Created Lectures & Notes')

        # Step 7: Assignments & Grading
        now = timezone.now()
        for classroom, enrolled_students in [(class_a, class_a_students), (class_b, class_b_students)]:
            for i in range(2):
                assignment, _ = Assignment.objects.get_or_create(
                    title=f"Assignment {i+1} - {classroom.class_code}",
                    classroom=classroom,
                    defaults={
                        "created_by": classroom.teacher,
                        "description": fake.text(),
                        "instructions": fake.sentence(),
                        "due_date": now + timedelta(days=7),
                        "total_marks": 100,
                        "pass_marks": 40,
                        "is_published": True,
                        "published_at": now
                    }
                )
                
                for student in enrolled_students:
                    submission, _ = AssignmentSubmission.objects.get_or_create(
                        assignment=assignment,
                        student=student,
                        defaults={
                            "status": "graded",
                            "submitted_at": now - timedelta(days=1),
                            "graded_at": now,
                            "answers": {"answer": fake.text()}
                        }
                    )
                    
                    AssignmentGrade.objects.get_or_create(
                        submission=submission,
                        defaults={
                            "score": random.randint(40, 100),
                            "max_score": 100,
                            "overall_feedback": fake.sentence(),
                            "graded_by": classroom.teacher,
                            "is_published": True,
                            "published_at": now
                        }
                    )
        self.stdout.write('Step 7: Created Assignments & Grading')

        # Step 8: Gamification (To populate the Leaderboard)
        for classroom, enrolled_students in [(class_a, class_a_students), (class_b, class_b_students)]:
            leaderboard, _ = Leaderboard.objects.get_or_create(
                name=f"Leaderboard {classroom.class_code}",
                leaderboard_type="xp",
                scope="classroom",
                classroom=classroom,
                defaults={"is_active": True, "max_entries": 10}
            )
            
            student_xp_totals = []
            
            for student in enrolled_students:
                xp_record, _ = StudentXP.objects.get_or_create(student=student)
                
                total_xp_for_student = xp_record.total_xp
                
                for _ in range(5):
                    amount = random.randint(10, 50)
                    total_xp_for_student += amount
                    XPTransaction.objects.get_or_create(
                        student=student,
                        transaction_type="earned",
                        source="assignment_completed",
                        description=fake.sentence(),
                        amount=amount,
                        balance_after=total_xp_for_student
                    )
                
                xp_record.total_xp = total_xp_for_student
                xp_record.save()
                student_xp_totals.append((student, total_xp_for_student))
            
            # Rank students by XP
            student_xp_totals.sort(key=lambda x: x[1], reverse=True)
            
            for rank, (student, score) in enumerate(student_xp_totals, start=1):
                LeaderboardEntry.objects.update_or_create(
                    leaderboard=leaderboard,
                    student=student,
                    defaults={"rank": rank, "score": score}
                )
                
        self.stdout.write('Step 8: Created Gamification XP & Leaderboards')
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully populated all dummy data!'))
