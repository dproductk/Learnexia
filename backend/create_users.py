from django.contrib.auth import get_user_model
from apps.accounts.models import StudentProfile, TeacherProfile

User = get_user_model()

def create_or_update_user(email, password, role, first_name, last_name, **profile_kwargs):
    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            'role': role,
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    user.set_password(password)
    user.save()
    
    if role == 'student':
        StudentProfile.objects.get_or_create(user=user, defaults=profile_kwargs)
    elif role == 'teacher':
        TeacherProfile.objects.get_or_create(user=user, defaults=profile_kwargs)
        
    status = "Created" if created else "Updated"
    print(f"{status} {role}: Email={email} Password={password}")

create_or_update_user('admin@learnexia.com', 'admin_pass_123', 'admin', 'System', 'Admin')
create_or_update_user('teacher@learnexia.com', 'teacher_pass_123', 'teacher', 'Demo', 'Teacher', employee_id='T_DEMO_01')
create_or_update_user('student@learnexia.com', 'student_pass_123', 'student', 'Demo', 'Student', grade=5)
print("User creation script finished.")
