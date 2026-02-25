# Database Schema Documentation

## PART 1 & 2 — Tables Overview and Columns Breakdown

### Table: `accounts_user` (accounts.User)

- **Purpose:** Model representing `User` in the `accounts` app.
- **Real-world entity:** Represents a user entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `password` | `CharField` | Stores the password | No | `-` | No | No | No | `-` | `-` |
| `last_login` | `DateTimeField` | Stores the last login | Yes | `-` | No | No | No | `-` | `-` |
| `is_superuser` | `BooleanField` | Designates that this user has all permissions without explicitly assigning them. | No | `False` | No | No | No | `-` | `-` |
| `first_name` | `CharField` | Stores the first name | No | `-` | No | No | No | `-` | `-` |
| `last_name` | `CharField` | Stores the last name | No | `-` | No | No | No | `-` | `-` |
| `is_staff` | `BooleanField` | Designates whether the user can log into this admin site. | No | `False` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | No | `True` | No | No | No | `-` | `-` |
| `date_joined` | `DateTimeField` | Stores the date joined | No | `<function now at 0x000001CC1B1C0C20>` | No | No | No | `-` | `-` |
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `email` | `CharField` | Stores the email | No | `-` | Yes | Yes | No | `-` | `-` |
| `role` | `CharField` | Stores the role | No | `-` | No | Yes | No | `-` | `-` |
| `phone_number` | `CharField` | Stores the phone number | No | `-` | No | No | No | `-` | `-` |
| `avatar` | `FileField` | Stores the avatar | Yes | `-` | No | No | No | `-` | `-` |
| `is_verified` | `BooleanField` | Stores the is verified | No | `False` | No | No | No | `-` | `-` |
| `last_login_ip` | `GenericIPAddressField` | Stores the last login ip | Yes | `-` | No | No | No | `-` | `-` |
| `groups` | `ManyToManyField` | The groups this user belongs to. A user will get all permissions granted to each of their groups. | No | `-` | No | No | No | `Group` | `-` |
| `user_permissions` | `ManyToManyField` | Specific permissions for this user. | No | `-` | No | No | No | `Permission` | `-` |

### Table: `accounts_studentprofile` (accounts.StudentProfile)

- **Purpose:** Model representing `StudentProfile` in the `accounts` app.
- **Real-world entity:** Represents a studentprofile entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `user` | `OneToOneField` | Stores the user | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `grade` | `IntegerField` | Stores the grade | Yes | `-` | No | No | No | `-` | `-` |
| `date_of_birth` | `DateField` | Stores the date of birth | Yes | `-` | No | No | No | `-` | `-` |
| `guardian_name` | `CharField` | Stores the guardian name | No | `-` | No | No | No | `-` | `-` |
| `guardian_relationship` | `CharField` | Stores the guardian relationship | No | `-` | No | No | No | `-` | `-` |
| `emergency_contact` | `CharField` | Stores the emergency contact | No | `-` | No | No | No | `-` | `-` |
| `address` | `TextField` | Stores the address | No | `-` | No | No | No | `-` | `-` |
| `medical_notes` | `TextField` | Stores the medical notes | No | `-` | No | No | No | `-` | `-` |
| `total_xp` | `PositiveIntegerField` | Stores the total xp | No | `0` | No | Yes | No | `-` | `-` |
| `current_level` | `PositiveIntegerField` | Stores the current level | No | `1` | No | No | No | `-` | `-` |
| `current_streak` | `PositiveIntegerField` | Stores the current streak | No | `0` | No | No | No | `-` | `-` |
| `longest_streak` | `PositiveIntegerField` | Stores the longest streak | No | `0` | No | No | No | `-` | `-` |
| `last_activity_date` | `DateField` | Stores the last activity date | Yes | `-` | No | No | No | `-` | `-` |

### Table: `accounts_teacherprofile` (accounts.TeacherProfile)

- **Purpose:** Model representing `TeacherProfile` in the `accounts` app.
- **Real-world entity:** Represents a teacherprofile entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `user` | `OneToOneField` | Stores the user | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `employee_id` | `CharField` | Stores the employee id | Yes | `-` | Yes | No | No | `-` | `-` |
| `specialization` | `CharField` | Stores the specialization | No | `-` | No | No | No | `-` | `-` |
| `qualification` | `CharField` | Stores the qualification | No | `-` | No | No | No | `-` | `-` |
| `years_of_experience` | `PositiveIntegerField` | Stores the years of experience | No | `0` | No | No | No | `-` | `-` |
| `date_of_joining` | `DateField` | Stores the date of joining | Yes | `-` | No | No | No | `-` | `-` |
| `bio` | `TextField` | Stores the bio | No | `-` | No | No | No | `-` | `-` |

### Table: `accounts_parentprofile` (accounts.ParentProfile)

- **Purpose:** Model representing `ParentProfile` in the `accounts` app.
- **Real-world entity:** Represents a parentprofile entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `user` | `OneToOneField` | Stores the user | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `occupation` | `CharField` | Stores the occupation | No | `-` | No | No | No | `-` | `-` |

### Table: `accounts_parentstudentrelationship` (accounts.ParentStudentRelationship)

- **Purpose:** Model representing `ParentStudentRelationship` in the `accounts` app.
- **Real-world entity:** Represents a parentstudentrelationship entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `parent` | `ForeignKey` | Stores the parent | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `relationship_type` | `CharField` | Stores the relationship type | No | `-` | No | No | No | `-` | `-` |
| `is_primary` | `BooleanField` | Stores the is primary | No | `False` | No | No | No | `-` | `-` |

### Table: `schools_school` (schools.School)

- **Purpose:** Model representing `School` in the `schools` app.
- **Real-world entity:** Represents a school entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | Yes | No | `-` | `-` |
| `code` | `CharField` | Stores the code | No | `-` | Yes | No | No | `-` | `-` |
| `address` | `TextField` | Stores the address | No | `-` | No | No | No | `-` | `-` |
| `city` | `CharField` | Stores the city | No | `-` | No | No | No | `-` | `-` |
| `state` | `CharField` | Stores the state | No | `-` | No | No | No | `-` | `-` |
| `country` | `CharField` | Stores the country | No | `India` | No | No | No | `-` | `-` |
| `pincode` | `CharField` | Stores the pincode | No | `-` | No | No | No | `-` | `-` |
| `phone` | `CharField` | Stores the phone | No | `-` | No | No | No | `-` | `-` |
| `email` | `CharField` | Stores the email | No | `-` | No | No | No | `-` | `-` |
| `website` | `CharField` | Stores the website | No | `-` | No | No | No | `-` | `-` |
| `logo` | `FileField` | Stores the logo | Yes | `-` | No | No | No | `-` | `-` |
| `principal_name` | `CharField` | Stores the principal name | No | `-` | No | No | No | `-` | `-` |
| `established_year` | `PositiveIntegerField` | Stores the established year | No | `-` | No | No | No | `-` | `-` |

### Table: `schools_academicyear` (schools.AcademicYear)

- **Purpose:** Model representing `AcademicYear` in the `schools` app.
- **Real-world entity:** Represents a academicyear entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `school` | `ForeignKey` | Stores the school | No | `-` | No | Yes | No | `School` | `CASCADE` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `start_date` | `DateField` | Stores the start date | No | `-` | No | No | No | `-` | `-` |
| `end_date` | `DateField` | Stores the end date | No | `-` | No | No | No | `-` | `-` |
| `is_current` | `BooleanField` | Stores the is current | No | `False` | No | Yes | No | `-` | `-` |

### Table: `schools_subject` (schools.Subject)

- **Purpose:** Model representing `Subject` in the `schools` app.
- **Real-world entity:** Represents a subject entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `code` | `CharField` | Stores the code | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `icon` | `CharField` | Stores the icon | No | `-` | No | No | No | `-` | `-` |
| `color` | `CharField` | Stores the color | No | `#3B82F6` | No | No | No | `-` | `-` |
| `grade` | `IntegerField` | Stores the grade | No | `-` | No | No | No | `-` | `-` |

### Table: `schools_classroom` (schools.Classroom)

- **Purpose:** Model representing `Classroom` in the `schools` app.
- **Real-world entity:** Represents a classroom entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `school` | `ForeignKey` | Stores the school | No | `-` | No | Yes | No | `School` | `CASCADE` |
| `academic_year` | `ForeignKey` | Stores the academic year | No | `-` | No | Yes | No | `AcademicYear` | `CASCADE` |
| `subject` | `ForeignKey` | Stores the subject | No | `-` | No | Yes | No | `Subject` | `CASCADE` |
| `grade` | `IntegerField` | Stores the grade | No | `-` | No | No | No | `-` | `-` |
| `section` | `CharField` | Stores the section | No | `-` | No | No | No | `-` | `-` |
| `teacher` | `ForeignKey` | Stores the teacher | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `room_number` | `CharField` | Stores the room number | No | `-` | No | No | No | `-` | `-` |
| `max_students` | `PositiveIntegerField` | Stores the max students | No | `30` | No | No | No | `-` | `-` |
| `class_code` | `CharField` | Stores the class code | No | `-` | Yes | No | No | `-` | `-` |

### Table: `schools_classroomenrollment` (schools.ClassroomEnrollment)

- **Purpose:** Model representing `ClassroomEnrollment` in the `schools` app.
- **Real-world entity:** Represents a classroomenrollment entity.
- **Type:** Core table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `enrollment_date` | `DateField` | Stores the enrollment date | No | `-` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | Yes | No | `-` | `-` |

### Table: `lectures_lecture` (lectures.Lecture)

- **Purpose:** Model representing `Lecture` in the `lectures` app.
- **Real-world entity:** Represents a lecture entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | Yes | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `chapter` | `CharField` | Stores the chapter | No | `-` | No | No | No | `-` | `-` |
| `topic` | `CharField` | Stores the topic | No | `-` | No | No | No | `-` | `-` |
| `recording_type` | `CharField` | Stores the recording type | No | `audio` | No | No | No | `-` | `-` |
| `audio_file` | `FileField` | Stores the audio file | Yes | `-` | No | No | No | `-` | `-` |
| `video_file` | `FileField` | Stores the video file | Yes | `-` | No | No | No | `-` | `-` |
| `thumbnail` | `FileField` | Stores the thumbnail | Yes | `-` | No | No | No | `-` | `-` |
| `duration` | `PositiveIntegerField` | Duration in seconds | Yes | `-` | No | No | No | `-` | `-` |
| `transcript` | `TextField` | Stores the transcript | No | `-` | No | No | No | `-` | `-` |
| `has_auto_generated_transcript` | `BooleanField` | Stores the has auto generated transcript | No | `False` | No | No | No | `-` | `-` |
| `transcript_status` | `CharField` | Stores the transcript status | No | `not_started` | No | Yes | No | `-` | `-` |
| `transcript_approved_by_teacher` | `BooleanField` | Teacher must approve transcript before AI features (notes, flashcards, quizzes) can use it | No | `False` | No | No | No | `-` | `-` |
| `transcript_approved_at` | `DateTimeField` | Stores the transcript approved at | Yes | `-` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `draft` | No | Yes | No | `-` | `-` |
| `scheduled_date` | `DateTimeField` | Stores the scheduled date | Yes | `-` | No | No | No | `-` | `-` |
| `is_live` | `BooleanField` | Stores the is live | No | `False` | No | Yes | No | `-` | `-` |
| `is_shared_with_students` | `BooleanField` | Stores the is shared with students | No | `False` | No | Yes | No | `-` | `-` |
| `shared_at` | `DateTimeField` | Stores the shared at | Yes | `-` | No | No | No | `-` | `-` |
| `notify_students` | `BooleanField` | Stores the notify students | No | `True` | No | No | No | `-` | `-` |
| `notify_parents` | `BooleanField` | Stores the notify parents | No | `False` | No | No | No | `-` | `-` |
| `view_count` | `PositiveIntegerField` | Stores the view count | No | `0` | No | No | No | `-` | `-` |
| `download_count` | `PositiveIntegerField` | Stores the download count | No | `0` | No | No | No | `-` | `-` |

### Table: `lectures_lecturebookmark` (lectures.LectureBookmark)

- **Purpose:** Model representing `LectureBookmark` in the `lectures` app.
- **Real-world entity:** Represents a lecturebookmark entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `created_by` | `ForeignKey` | Stores the created by | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `timestamp` | `PositiveIntegerField` | Timestamp in seconds | No | `-` | No | No | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `note` | `TextField` | Stores the note | No | `-` | No | No | No | `-` | `-` |

### Table: `lectures_lectureview` (lectures.LectureView)

- **Purpose:** Model representing `LectureView` in the `lectures` app.
- **Real-world entity:** Represents a lectureview entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `started_at` | `DateTimeField` | Stores the started at | No | `-` | No | No | No | `-` | `-` |
| `last_position` | `PositiveIntegerField` | Last watched position in seconds | No | `0` | No | No | No | `-` | `-` |
| `completed_at` | `DateTimeField` | Stores the completed at | Yes | `-` | No | No | No | `-` | `-` |
| `completion_percentage` | `PositiveIntegerField` | Stores the completion percentage | No | `0` | No | No | No | `-` | `-` |
| `watch_time` | `PositiveIntegerField` | Total watch time in seconds | No | `0` | No | No | No | `-` | `-` |

### Table: `lectures_lectureresource` (lectures.LectureResource)

- **Purpose:** Model representing `LectureResource` in the `lectures` app.
- **Real-world entity:** Represents a lectureresource entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `file` | `FileField` | Stores the file | No | `-` | No | No | No | `-` | `-` |
| `file_type` | `CharField` | Stores the file type | No | `-` | No | No | No | `-` | `-` |
| `file_size` | `PositiveIntegerField` | File size in bytes | No | `-` | No | No | No | `-` | `-` |

### Table: `notes_notetemplate` (notes.NoteTemplate)

- **Purpose:** Model representing `NoteTemplate` in the `notes` app.
- **Real-world entity:** Represents a notetemplate entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `content` | `TextField` | Template content in HTML/Markdown | No | `-` | No | No | No | `-` | `-` |
| `is_default` | `BooleanField` | Stores the is default | No | `False` | No | No | No | `-` | `-` |
| `created_by` | `ForeignKey` | Stores the created by | No | `-` | No | Yes | No | `User` | `CASCADE` |

### Table: `notes_lecturenote` (notes.LectureNote)

- **Purpose:** Model representing `LectureNote` in the `notes` app.
- **Real-world entity:** Represents a lecturenote entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `lecture` | `OneToOneField` | Stores the lecture | No | `-` | Yes | Yes | No | `Lecture` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `content` | `TextField` | Rich text content | No | `-` | No | No | No | `-` | `-` |
| `summary` | `TextField` | Stores the summary | No | `-` | No | No | No | `-` | `-` |
| `template` | `ForeignKey` | Stores the template | Yes | `-` | No | Yes | No | `NoteTemplate` | `SET_NULL` |
| `is_auto_generated` | `BooleanField` | Stores the is auto generated | No | `False` | No | No | No | `-` | `-` |
| `auto_generated_at` | `DateTimeField` | Stores the auto generated at | Yes | `-` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | Yes | No | `-` | `-` |
| `published_at` | `DateTimeField` | Stores the published at | Yes | `-` | No | No | No | `-` | `-` |
| `pdf_file` | `FileField` | Stores the pdf file | Yes | `-` | No | No | No | `-` | `-` |
| `pdf_generated_at` | `DateTimeField` | Stores the pdf generated at | Yes | `-` | No | No | No | `-` | `-` |
| `view_count` | `PositiveIntegerField` | Stores the view count | No | `0` | No | No | No | `-` | `-` |
| `download_count` | `PositiveIntegerField` | Stores the download count | No | `0` | No | No | No | `-` | `-` |
| `bookmark_count` | `PositiveIntegerField` | Stores the bookmark count | No | `0` | No | No | No | `-` | `-` |

### Table: `notes_studentnotebookmark` (notes.StudentNoteBookmark)

- **Purpose:** Model representing `StudentNoteBookmark` in the `notes` app.
- **Real-world entity:** Represents a studentnotebookmark entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `note` | `ForeignKey` | Stores the note | No | `-` | No | Yes | No | `LectureNote` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |

### Table: `notes_studentnoteview` (notes.StudentNoteView)

- **Purpose:** Model representing `StudentNoteView` in the `notes` app.
- **Real-world entity:** Represents a studentnoteview entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `note` | `ForeignKey` | Stores the note | No | `-` | No | Yes | No | `LectureNote` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `viewed_at` | `DateTimeField` | Stores the viewed at | No | `-` | No | No | No | `-` | `-` |
| `time_spent` | `PositiveIntegerField` | Time spent reading in seconds | No | `0` | No | No | No | `-` | `-` |

### Table: `notes_studentpersonalnote` (notes.StudentPersonalNote)

- **Purpose:** Model representing `StudentPersonalNote` in the `notes` app.
- **Real-world entity:** Represents a studentpersonalnote entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `lecture_note` | `ForeignKey` | Stores the lecture note | No | `-` | No | Yes | No | `LectureNote` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `content` | `TextField` | Stores the content | No | `-` | No | No | No | `-` | `-` |
| `highlighted_text` | `TextField` | Stores the highlighted text | No | `-` | No | No | No | `-` | `-` |
| `position` | `JSONField` | Position in the document | Yes | `-` | No | No | No | `-` | `-` |

### Table: `flashcards_flashcardset` (flashcards.FlashcardSet)

- **Purpose:** Model representing `FlashcardSet` in the `flashcards` app.
- **Real-world entity:** Represents a flashcardset entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | Yes | No | `-` | `-` |
| `published_at` | `DateTimeField` | Stores the published at | Yes | `-` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |
| `ai_generated_at` | `DateTimeField` | Stores the ai generated at | Yes | `-` | No | No | No | `-` | `-` |
| `view_count` | `PositiveIntegerField` | Stores the view count | No | `0` | No | No | No | `-` | `-` |
| `study_count` | `PositiveIntegerField` | Stores the study count | No | `0` | No | No | No | `-` | `-` |

### Table: `flashcards_flashcard` (flashcards.Flashcard)

- **Purpose:** Model representing `Flashcard` in the `flashcards` app.
- **Real-world entity:** Represents a flashcard entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `flashcard_set` | `ForeignKey` | Stores the flashcard set | No | `-` | No | Yes | No | `FlashcardSet` | `CASCADE` |
| `question` | `TextField` | Front of the card | No | `-` | No | No | No | `-` | `-` |
| `answer` | `TextField` | Back of the card | No | `-` | No | No | No | `-` | `-` |
| `hint` | `TextField` | Stores the hint | No | `-` | No | No | No | `-` | `-` |
| `order` | `PositiveIntegerField` | Stores the order | No | `0` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |

### Table: `flashcards_studentflashcardprogress` (flashcards.StudentFlashcardProgress)

- **Purpose:** Model representing `StudentFlashcardProgress` in the `flashcards` app.
- **Real-world entity:** Represents a studentflashcardprogress entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `flashcard` | `ForeignKey` | Stores the flashcard | No | `-` | No | Yes | No | `Flashcard` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `confidence_level` | `CharField` | Stores the confidence level | No | `not_studied` | No | No | No | `-` | `-` |
| `times_studied` | `PositiveIntegerField` | Stores the times studied | No | `0` | No | No | No | `-` | `-` |
| `times_correct` | `PositiveIntegerField` | Stores the times correct | No | `0` | No | No | No | `-` | `-` |
| `times_incorrect` | `PositiveIntegerField` | Stores the times incorrect | No | `0` | No | No | No | `-` | `-` |
| `last_studied_at` | `DateTimeField` | Stores the last studied at | Yes | `-` | No | No | No | `-` | `-` |
| `next_review_at` | `DateTimeField` | Stores the next review at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `flashcards_studentflashcardsetview` (flashcards.StudentFlashcardSetView)

- **Purpose:** Model representing `StudentFlashcardSetView` in the `flashcards` app.
- **Real-world entity:** Represents a studentflashcardsetview entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `flashcard_set` | `ForeignKey` | Stores the flashcard set | No | `-` | No | Yes | No | `FlashcardSet` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `viewed_at` | `DateTimeField` | Stores the viewed at | No | `-` | No | No | No | `-` | `-` |
| `time_spent` | `PositiveIntegerField` | Time spent studying in seconds | No | `0` | No | No | No | `-` | `-` |
| `cards_studied` | `PositiveIntegerField` | Stores the cards studied | No | `0` | No | No | No | `-` | `-` |

### Table: `games_gametemplate` (games.GameTemplate)

- **Purpose:** Model representing `GameTemplate` in the `games` app.
- **Real-world entity:** Represents a gametemplate entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `code` | `CharField` | Stores the code | No | `-` | Yes | Yes | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `icon` | `CharField` | Emoji or icon class | No | `-` | No | No | No | `-` | `-` |
| `game_type` | `CharField` | Stores the game type | No | `-` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | Yes | No | `-` | `-` |
| `min_questions` | `PositiveIntegerField` | Stores the min questions | No | `5` | No | No | No | `-` | `-` |
| `max_questions` | `PositiveIntegerField` | Stores the max questions | No | `20` | No | No | No | `-` | `-` |
| `default_time_per_question` | `PositiveIntegerField` | Default time limit in seconds | No | `8` | No | No | No | `-` | `-` |
| `supports_difficulty` | `BooleanField` | Stores the supports difficulty | No | `True` | No | No | No | `-` | `-` |

### Table: `games_lecturegame` (games.LectureGame)

- **Purpose:** Model representing `LectureGame` in the `games` app.
- **Real-world entity:** Represents a lecturegame entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `template` | `ForeignKey` | Stores the template | No | `-` | No | Yes | No | `GameTemplate` | `PROTECT` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `difficulty` | `CharField` | Stores the difficulty | No | `MEDIUM` | No | Yes | No | `-` | `-` |
| `question_count` | `PositiveIntegerField` | Stores the question count | No | `-` | No | No | No | `-` | `-` |
| `game_data` | `JSONField` | Stores all game content (questions, config, etc.) | No | `-` | No | No | No | `-` | `-` |
| `estimated_duration` | `PositiveIntegerField` | Estimated duration in minutes | No | `5` | No | No | No | `-` | `-` |
| `generated_by` | `ForeignKey` | Stores the generated by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `generated_at` | `DateTimeField` | Stores the generated at | No | `-` | No | No | No | `-` | `-` |
| `ai_model_used` | `CharField` | Stores the ai model used | No | `gemini-1.5-flash` | No | No | No | `-` | `-` |
| `ai_generation_cost` | `DecimalField` | Stores the ai generation cost | No | `0.0000` | No | No | No | `-` | `-` |
| `prompt_tokens` | `PositiveIntegerField` | Stores the prompt tokens | No | `0` | No | No | No | `-` | `-` |
| `completion_tokens` | `PositiveIntegerField` | Stores the completion tokens | No | `0` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | Yes | No | `-` | `-` |
| `published_at` | `DateTimeField` | Stores the published at | Yes | `-` | No | No | No | `-` | `-` |
| `published_by` | `ForeignKey` | Stores the published by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `total_plays` | `PositiveIntegerField` | Stores the total plays | No | `0` | No | No | No | `-` | `-` |
| `total_completions` | `PositiveIntegerField` | Stores the total completions | No | `0` | No | No | No | `-` | `-` |
| `average_score` | `DecimalField` | Stores the average score | No | `0.00` | No | No | No | `-` | `-` |
| `average_completion_time` | `PositiveIntegerField` | Average completion time in seconds | No | `0` | No | No | No | `-` | `-` |
| `highest_score` | `PositiveIntegerField` | Stores the highest score | No | `0` | No | No | No | `-` | `-` |
| `highest_scorer` | `ForeignKey` | Stores the highest scorer | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `games_gameattempt` (games.GameAttempt)

- **Purpose:** Model representing `GameAttempt` in the `games` app.
- **Real-world entity:** Represents a gameattempt entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `lecture_game` | `ForeignKey` | Stores the lecture game | No | `-` | No | Yes | No | `LectureGame` | `CASCADE` |
| `started_at` | `DateTimeField` | Stores the started at | No | `-` | No | No | No | `-` | `-` |
| `completed_at` | `DateTimeField` | Stores the completed at | Yes | `-` | No | No | No | `-` | `-` |
| `is_completed` | `BooleanField` | Stores the is completed | No | `False` | No | Yes | No | `-` | `-` |
| `final_score` | `PositiveIntegerField` | Stores the final score | No | `0` | No | No | No | `-` | `-` |
| `max_possible_score` | `PositiveIntegerField` | Stores the max possible score | No | `0` | No | No | No | `-` | `-` |
| `accuracy_percentage` | `DecimalField` | Stores the accuracy percentage | No | `0.00` | No | No | No | `-` | `-` |
| `time_taken` | `PositiveIntegerField` | Time taken in seconds | No | `0` | No | No | No | `-` | `-` |
| `questions_answered` | `PositiveIntegerField` | Stores the questions answered | No | `0` | No | No | No | `-` | `-` |
| `correct_answers` | `PositiveIntegerField` | Stores the correct answers | No | `0` | No | No | No | `-` | `-` |
| `wrong_answers` | `PositiveIntegerField` | Stores the wrong answers | No | `0` | No | No | No | `-` | `-` |
| `max_combo_achieved` | `PositiveIntegerField` | Stores the max combo achieved | No | `0` | No | No | No | `-` | `-` |
| `lives_remaining` | `PositiveIntegerField` | Stores the lives remaining | No | `0` | No | No | No | `-` | `-` |
| `detailed_results` | `JSONField` | Question-by-question breakdown | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `performance_metrics` | `JSONField` | Advanced performance metrics | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `xp_earned` | `PositiveIntegerField` | Stores the xp earned | No | `0` | No | No | No | `-` | `-` |
| `rank_achieved` | `PositiveIntegerField` | Position in leaderboard | Yes | `-` | No | No | No | `-` | `-` |

### Table: `games_gameleaderboard` (games.GameLeaderboard)

- **Purpose:** Model representing `GameLeaderboard` in the `games` app.
- **Real-world entity:** Represents a gameleaderboard entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `lecture_game` | `ForeignKey` | Stores the lecture game | No | `-` | No | Yes | No | `LectureGame` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `rank` | `PositiveIntegerField` | Stores the rank | No | `-` | No | Yes | No | `-` | `-` |
| `best_score` | `PositiveIntegerField` | Stores the best score | No | `0` | No | No | No | `-` | `-` |
| `best_attempt` | `ForeignKey` | Stores the best attempt | Yes | `-` | No | Yes | No | `GameAttempt` | `SET_NULL` |
| `total_plays` | `PositiveIntegerField` | Stores the total plays | No | `0` | No | No | No | `-` | `-` |
| `last_played` | `DateTimeField` | Stores the last played | No | `-` | No | No | No | `-` | `-` |

### Table: `assignments_assignment` (assignments.Assignment)

- **Purpose:** Model representing `Assignment` in the `assignments` app.
- **Real-world entity:** Represents a assignment entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | Yes | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `instructions` | `TextField` | Stores the instructions | No | `-` | No | No | No | `-` | `-` |
| `created_by` | `ForeignKey` | Stores the created by | Yes | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `source_lecture` | `ForeignKey` | If AI-generated, the lecture it was based on | Yes | `-` | No | Yes | No | `Lecture` | `SET_NULL` |
| `submission_type` | `CharField` | Stores the submission type | No | `online` | No | No | No | `-` | `-` |
| `difficulty` | `CharField` | Stores the difficulty | Yes | `-` | No | No | No | `-` | `-` |
| `assignment_format` | `CharField` | Stores the assignment format | No | `short_answer` | No | No | No | `-` | `-` |
| `total_marks` | `PositiveIntegerField` | Stores the total marks | No | `10` | No | No | No | `-` | `-` |
| `pass_marks` | `PositiveIntegerField` | Stores the pass marks | No | `6` | No | No | No | `-` | `-` |
| `grading_method` | `CharField` | Stores the grading method | No | `ai_assisted` | No | No | No | `-` | `-` |
| `grading_type` | `CharField` | Stores the grading type | No | `basic` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |
| `ai_generation_prompt` | `TextField` | Stores the ai generation prompt | No | `-` | No | No | No | `-` | `-` |
| `ai_generation_cost` | `DecimalField` | Cost in USD | No | `0` | No | No | No | `-` | `-` |
| `generation_tokens` | `IntegerField` | Stores the generation tokens | No | `0` | No | No | No | `-` | `-` |
| `ai_generated_at` | `DateTimeField` | Stores the ai generated at | Yes | `-` | No | No | No | `-` | `-` |
| `due_date` | `DateTimeField` | Stores the due date | No | `-` | No | Yes | No | `-` | `-` |
| `allow_late_submission` | `BooleanField` | Stores the allow late submission | No | `False` | No | No | No | `-` | `-` |
| `late_penalty_per_day` | `PositiveIntegerField` | Percentage penalty per day late | No | `10` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | No | No | `-` | `-` |
| `published_at` | `DateTimeField` | Stores the published at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `assignments_assignmentquestion` (assignments.AssignmentQuestion)

- **Purpose:** Model representing `AssignmentQuestion` in the `assignments` app.
- **Real-world entity:** Represents a assignmentquestion entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `assignment` | `ForeignKey` | Stores the assignment | No | `-` | No | Yes | No | `Assignment` | `CASCADE` |
| `question_number` | `PositiveIntegerField` | Stores the question number | No | `-` | No | No | No | `-` | `-` |
| `question_text` | `TextField` | Stores the question text | No | `-` | No | No | No | `-` | `-` |
| `expected_answer_keywords` | `JSONField` | Keywords AI should look for when grading | No | `<class 'list'>` | No | No | No | `-` | `-` |
| `expected_answer_length` | `CharField` | e.g., "2-3 sentences", "1 paragraph" | No | `-` | No | No | No | `-` | `-` |
| `grading_notes` | `TextField` | Criteria for full marks | No | `-` | No | No | No | `-` | `-` |
| `marks` | `DecimalField` | Leave blank for equal distribution | Yes | `-` | No | No | No | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | No | No | `-` | `-` |

### Table: `assignments_rubriccriterion` (assignments.RubricCriterion)

- **Purpose:** Model representing `RubricCriterion` in the `assignments` app.
- **Real-world entity:** Represents a rubriccriterion entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `assignment` | `ForeignKey` | Stores the assignment | No | `-` | No | Yes | No | `Assignment` | `CASCADE` |
| `criterion_name` | `CharField` | e.g., Content Accuracy, Grammar, Structure | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `weight_percentage` | `PositiveIntegerField` | Percentage weight (all criteria must sum to 100) | No | `-` | No | No | No | `-` | `-` |
| `order` | `PositiveIntegerField` | Stores the order | No | `0` | No | No | No | `-` | `-` |

### Table: `assignments_assignmentsubmission` (assignments.AssignmentSubmission)

- **Purpose:** Model representing `AssignmentSubmission` in the `assignments` app.
- **Real-world entity:** Represents a assignmentsubmission entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `assignment` | `ForeignKey` | Stores the assignment | No | `-` | No | Yes | No | `Assignment` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `submission_method` | `CharField` | For online assignments: how student submitted (text vs PDF) | Yes | `-` | No | No | No | `-` | `-` |
| `answers` | `JSONField` | For text: {question_id: answer_text}. For PDF: {metadata: {...}} | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `uploaded_file` | `FileField` | PDF file for both online-PDF and offline submissions | Yes | `-` | No | No | No | `-` | `-` |
| `file_size_bytes` | `PositiveIntegerField` | Stores the file size bytes | Yes | `-` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `draft` | No | Yes | No | `-` | `-` |
| `submitted_at` | `DateTimeField` | Stores the submitted at | Yes | `-` | No | No | No | `-` | `-` |
| `graded_at` | `DateTimeField` | Stores the graded at | Yes | `-` | No | No | No | `-` | `-` |
| `is_late` | `BooleanField` | Stores the is late | No | `False` | No | No | No | `-` | `-` |
| `days_late` | `PositiveIntegerField` | Stores the days late | No | `0` | No | No | No | `-` | `-` |

### Table: `assignments_assignmentgrade` (assignments.AssignmentGrade)

- **Purpose:** Model representing `AssignmentGrade` in the `assignments` app.
- **Real-world entity:** Represents a assignmentgrade entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `submission` | `OneToOneField` | Stores the submission | No | `-` | Yes | Yes | No | `AssignmentSubmission` | `CASCADE` |
| `score` | `DecimalField` | Stores the score | No | `-` | No | No | No | `-` | `-` |
| `max_score` | `DecimalField` | Stores the max score | No | `-` | No | No | No | `-` | `-` |
| `percentage` | `DecimalField` | Stores the percentage | No | `-` | No | No | No | `-` | `-` |
| `overall_feedback` | `TextField` | Stores the overall feedback | No | `-` | No | No | No | `-` | `-` |
| `teacher_comments` | `TextField` | Stores the teacher comments | No | `-` | No | No | No | `-` | `-` |
| `ai_suggested_score` | `DecimalField` | Stores the ai suggested score | Yes | `-` | No | No | No | `-` | `-` |
| `ai_feedback` | `TextField` | Stores the ai feedback | No | `-` | No | No | No | `-` | `-` |
| `ai_grading_data` | `JSONField` | Detailed AI analysis and scoring breakdown | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `ai_grading_cost` | `DecimalField` | Stores the ai grading cost | No | `0` | No | No | No | `-` | `-` |
| `ai_grading_tokens` | `IntegerField` | Stores the ai grading tokens | No | `0` | No | No | No | `-` | `-` |
| `graded_by` | `ForeignKey` | Stores the graded by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `teacher_modified_ai_score` | `BooleanField` | True if teacher changed AI suggestion | No | `False` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | No | No | `-` | `-` |
| `published_at` | `DateTimeField` | Stores the published at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `assignments_rubricscore` (assignments.RubricScore)

- **Purpose:** Model representing `RubricScore` in the `assignments` app.
- **Real-world entity:** Represents a rubricscore entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `grade` | `ForeignKey` | Stores the grade | No | `-` | No | Yes | No | `AssignmentGrade` | `CASCADE` |
| `criterion` | `ForeignKey` | Stores the criterion | No | `-` | No | Yes | No | `RubricCriterion` | `CASCADE` |
| `score` | `DecimalField` | Stores the score | No | `-` | No | No | No | `-` | `-` |
| `ai_suggested_score` | `DecimalField` | Stores the ai suggested score | Yes | `-` | No | No | No | `-` | `-` |
| `feedback` | `TextField` | Stores the feedback | No | `-` | No | No | No | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | No | No | `-` | `-` |

### Table: `assignments_gradingauditlog` (assignments.GradingAuditLog)

- **Purpose:** Model representing `GradingAuditLog` in the `assignments` app.
- **Real-world entity:** Represents a gradingauditlog entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `grade` | `ForeignKey` | Stores the grade | No | `-` | No | Yes | No | `AssignmentGrade` | `CASCADE` |
| `action` | `CharField` | Stores the action | No | `-` | No | No | No | `-` | `-` |
| `performed_by` | `ForeignKey` | Stores the performed by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `old_score` | `DecimalField` | Stores the old score | Yes | `-` | No | No | No | `-` | `-` |
| `new_score` | `DecimalField` | Stores the new score | Yes | `-` | No | No | No | `-` | `-` |
| `notes` | `TextField` | Stores the notes | No | `-` | No | No | No | `-` | `-` |
| `timestamp` | `DateTimeField` | Stores the timestamp | No | `-` | No | No | No | `-` | `-` |

### Table: `assessments_quiz` (assessments.Quiz)

- **Purpose:** Model representing `Quiz` in the `assessments` app.
- **Real-world entity:** Represents a quiz entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `title` | `CharField` | Stores the title | No | `-` | No | Yes | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `chapter` | `CharField` | Stores the chapter | No | `-` | No | No | No | `-` | `-` |
| `total_points` | `PositiveIntegerField` | Stores the total points | No | `100` | No | No | No | `-` | `-` |
| `time_limit` | `PositiveIntegerField` | Time limit in minutes | Yes | `-` | No | No | No | `-` | `-` |
| `passing_percentage` | `PositiveIntegerField` | Stores the passing percentage | No | `50` | No | No | No | `-` | `-` |
| `difficulty_level` | `CharField` | Stores the difficulty level | No | `medium` | No | No | No | `-` | `-` |
| `is_published` | `BooleanField` | Stores the is published | No | `False` | No | Yes | No | `-` | `-` |
| `available_from` | `DateTimeField` | Stores the available from | Yes | `-` | No | No | No | `-` | `-` |
| `available_until` | `DateTimeField` | Stores the available until | Yes | `-` | No | No | No | `-` | `-` |
| `allow_retake` | `BooleanField` | Stores the allow retake | No | `True` | No | No | No | `-` | `-` |
| `max_attempts` | `PositiveIntegerField` | Stores the max attempts | No | `3` | No | No | No | `-` | `-` |
| `show_correct_answers` | `BooleanField` | Stores the show correct answers | No | `True` | No | No | No | `-` | `-` |
| `shuffle_questions` | `BooleanField` | Stores the shuffle questions | No | `False` | No | No | No | `-` | `-` |
| `shuffle_options` | `BooleanField` | Stores the shuffle options | No | `False` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |
| `ai_generated_at` | `DateTimeField` | Stores the ai generated at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `assessments_question` (assessments.Question)

- **Purpose:** Model representing `Question` in the `assessments` app.
- **Real-world entity:** Represents a question entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `quiz` | `ForeignKey` | Stores the quiz | No | `-` | No | Yes | No | `Quiz` | `CASCADE` |
| `question_type` | `CharField` | Stores the question type | No | `-` | No | No | No | `-` | `-` |
| `question_text` | `TextField` | Stores the question text | No | `-` | No | No | No | `-` | `-` |
| `explanation` | `TextField` | Explanation shown after answering | No | `-` | No | No | No | `-` | `-` |
| `points` | `PositiveIntegerField` | Stores the points | No | `1` | No | No | No | `-` | `-` |
| `order` | `PositiveIntegerField` | Stores the order | No | `0` | No | No | No | `-` | `-` |
| `correct_answer_text` | `TextField` | Stores the correct answer text | No | `-` | No | No | No | `-` | `-` |
| `is_case_sensitive` | `BooleanField` | Stores the is case sensitive | No | `False` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |

### Table: `assessments_questionoption` (assessments.QuestionOption)

- **Purpose:** Model representing `QuestionOption` in the `assessments` app.
- **Real-world entity:** Represents a questionoption entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `question` | `ForeignKey` | Stores the question | No | `-` | No | Yes | No | `Question` | `CASCADE` |
| `option_text` | `TextField` | Stores the option text | No | `-` | No | No | No | `-` | `-` |
| `is_correct` | `BooleanField` | Stores the is correct | No | `False` | No | No | No | `-` | `-` |
| `order` | `PositiveIntegerField` | Stores the order | No | `0` | No | No | No | `-` | `-` |

### Table: `assessments_quizattempt` (assessments.QuizAttempt)

- **Purpose:** Model representing `QuizAttempt` in the `assessments` app.
- **Real-world entity:** Represents a quizattempt entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `quiz` | `ForeignKey` | Stores the quiz | No | `-` | No | Yes | No | `Quiz` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `attempt_number` | `PositiveIntegerField` | Stores the attempt number | No | `1` | No | No | No | `-` | `-` |
| `started_at` | `DateTimeField` | Stores the started at | No | `-` | No | No | No | `-` | `-` |
| `submitted_at` | `DateTimeField` | Stores the submitted at | Yes | `-` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `in_progress` | No | Yes | No | `-` | `-` |
| `total_points` | `DecimalField` | Stores the total points | No | `0` | No | No | No | `-` | `-` |
| `points_earned` | `DecimalField` | Stores the points earned | No | `0` | No | No | No | `-` | `-` |
| `percentage` | `DecimalField` | Stores the percentage | No | `0` | No | No | No | `-` | `-` |
| `time_taken` | `PositiveIntegerField` | Time taken in seconds | No | `0` | No | No | No | `-` | `-` |
| `is_ai_graded` | `BooleanField` | Stores the is ai graded | No | `False` | No | No | No | `-` | `-` |

### Table: `assessments_quizanswer` (assessments.QuizAnswer)

- **Purpose:** Model representing `QuizAnswer` in the `assessments` app.
- **Real-world entity:** Represents a quizanswer entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `attempt` | `ForeignKey` | Stores the attempt | No | `-` | No | Yes | No | `QuizAttempt` | `CASCADE` |
| `question` | `ForeignKey` | Stores the question | No | `-` | No | Yes | No | `Question` | `CASCADE` |
| `selected_option` | `ForeignKey` | Stores the selected option | Yes | `-` | No | Yes | No | `QuestionOption` | `CASCADE` |
| `answer_text` | `TextField` | Stores the answer text | No | `-` | No | No | No | `-` | `-` |
| `is_correct` | `BooleanField` | Stores the is correct | No | `False` | No | No | No | `-` | `-` |
| `points_earned` | `DecimalField` | Stores the points earned | No | `0` | No | No | No | `-` | `-` |
| `answered_at` | `DateTimeField` | Stores the answered at | No | `-` | No | No | No | `-` | `-` |
| `time_taken` | `PositiveIntegerField` | Time taken in seconds | No | `0` | No | No | No | `-` | `-` |
| `is_ai_graded` | `BooleanField` | Stores the is ai graded | No | `False` | No | No | No | `-` | `-` |
| `ai_feedback` | `TextField` | Stores the ai feedback | No | `-` | No | No | No | `-` | `-` |

### Table: `gamification_studentxp` (gamification.StudentXP)

- **Purpose:** Model representing `StudentXP` in the `gamification` app.
- **Real-world entity:** Represents a studentxp entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `OneToOneField` | Stores the student | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `total_xp` | `PositiveIntegerField` | Stores the total xp | No | `0` | No | Yes | No | `-` | `-` |
| `current_level` | `PositiveIntegerField` | Stores the current level | No | `1` | No | No | No | `-` | `-` |
| `xp_to_next_level` | `PositiveIntegerField` | Stores the xp to next level | No | `100` | No | No | No | `-` | `-` |
| `current_streak` | `PositiveIntegerField` | Consecutive days active | No | `0` | No | No | No | `-` | `-` |
| `longest_streak` | `PositiveIntegerField` | Stores the longest streak | No | `0` | No | No | No | `-` | `-` |
| `last_activity_date` | `DateField` | Stores the last activity date | Yes | `-` | No | No | No | `-` | `-` |
| `total_badges_earned` | `PositiveIntegerField` | Stores the total badges earned | No | `0` | No | No | No | `-` | `-` |
| `total_achievements` | `PositiveIntegerField` | Stores the total achievements | No | `0` | No | No | No | `-` | `-` |

### Table: `gamification_xptransaction` (gamification.XPTransaction)

- **Purpose:** Model representing `XPTransaction` in the `gamification` app.
- **Real-world entity:** Represents a xptransaction entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `transaction_type` | `CharField` | Stores the transaction type | No | `-` | No | No | No | `-` | `-` |
| `source` | `CharField` | Stores the source | No | `-` | No | No | No | `-` | `-` |
| `amount` | `IntegerField` | Positive for earned, negative for spent | No | `-` | No | No | No | `-` | `-` |
| `balance_after` | `PositiveIntegerField` | Total XP after transaction | No | `-` | No | No | No | `-` | `-` |
| `description` | `CharField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `reference_type` | `CharField` | assignment, quiz, etc. | No | `-` | No | No | No | `-` | `-` |
| `reference_id` | `CharField` | Stores the reference id | No | `-` | No | No | No | `-` | `-` |
| `awarded_by` | `ForeignKey` | Stores the awarded by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `gamification_badge` (gamification.Badge)

- **Purpose:** Model representing `Badge` in the `gamification` app.
- **Real-world entity:** Represents a badge entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | Yes | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `category` | `CharField` | Stores the category | No | `-` | No | Yes | No | `-` | `-` |
| `rarity` | `CharField` | Stores the rarity | No | `common` | No | No | No | `-` | `-` |
| `requirement_description` | `TextField` | What student needs to do to earn this | No | `-` | No | No | No | `-` | `-` |
| `xp_reward` | `PositiveIntegerField` | Stores the xp reward | No | `50` | No | No | No | `-` | `-` |
| `icon` | `CharField` | Icon name/class | No | `trophy` | No | No | No | `-` | `-` |
| `color` | `CharField` | Hex color code | No | `#FFD700` | No | No | No | `-` | `-` |
| `image` | `FileField` | Stores the image | Yes | `-` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |
| `is_secret` | `BooleanField` | Hidden until earned | No | `False` | No | No | No | `-` | `-` |
| `times_earned` | `PositiveIntegerField` | Stores the times earned | No | `0` | No | No | No | `-` | `-` |

### Table: `gamification_studentbadge` (gamification.StudentBadge)

- **Purpose:** Model representing `StudentBadge` in the `gamification` app.
- **Real-world entity:** Represents a studentbadge entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `badge` | `ForeignKey` | Stores the badge | No | `-` | No | Yes | No | `Badge` | `CASCADE` |
| `earned_at` | `DateTimeField` | Stores the earned at | No | `-` | No | No | No | `-` | `-` |
| `earned_for` | `CharField` | What action earned this badge | No | `-` | No | No | No | `-` | `-` |
| `reference_type` | `CharField` | Stores the reference type | No | `-` | No | No | No | `-` | `-` |
| `reference_id` | `CharField` | Stores the reference id | No | `-` | No | No | No | `-` | `-` |
| `is_displayed` | `BooleanField` | Show on student profile | No | `True` | No | No | No | `-` | `-` |
| `display_order` | `PositiveIntegerField` | Stores the display order | No | `0` | No | No | No | `-` | `-` |

### Table: `gamification_leaderboard` (gamification.Leaderboard)

- **Purpose:** Model representing `Leaderboard` in the `gamification` app.
- **Real-world entity:** Represents a leaderboard entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `leaderboard_type` | `CharField` | Stores the leaderboard type | No | `-` | No | No | No | `-` | `-` |
| `scope` | `CharField` | Stores the scope | No | `-` | No | No | No | `-` | `-` |
| `time_period` | `CharField` | Stores the time period | No | `all_time` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `grade_level` | `CharField` | Stores the grade level | No | `-` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |
| `max_entries` | `PositiveIntegerField` | Top N students to show | No | `10` | No | No | No | `-` | `-` |
| `last_updated` | `DateTimeField` | Stores the last updated | No | `-` | No | No | No | `-` | `-` |

### Table: `gamification_leaderboardentry` (gamification.LeaderboardEntry)

- **Purpose:** Model representing `LeaderboardEntry` in the `gamification` app.
- **Real-world entity:** Represents a leaderboardentry entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `leaderboard` | `ForeignKey` | Stores the leaderboard | No | `-` | No | Yes | No | `Leaderboard` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `rank` | `PositiveIntegerField` | Stores the rank | No | `-` | No | Yes | No | `-` | `-` |
| `score` | `PositiveIntegerField` | XP, badges count, etc. | No | `-` | No | No | No | `-` | `-` |
| `previous_rank` | `PositiveIntegerField` | Stores the previous rank | Yes | `-` | No | No | No | `-` | `-` |
| `rank_change` | `IntegerField` | Positive = moved up, negative = moved down | No | `0` | No | No | No | `-` | `-` |

### Table: `gamification_achievement` (gamification.Achievement)

- **Purpose:** Model representing `Achievement` in the `gamification` app.
- **Real-world entity:** Represents a achievement entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `requirement_type` | `CharField` | Stores the requirement type | No | `-` | No | No | No | `-` | `-` |
| `requirement_value` | `PositiveIntegerField` | Stores the requirement value | No | `-` | No | No | No | `-` | `-` |
| `xp_reward` | `PositiveIntegerField` | Stores the xp reward | No | `100` | No | No | No | `-` | `-` |
| `badge_reward` | `ForeignKey` | Stores the badge reward | Yes | `-` | No | Yes | No | `Badge` | `SET_NULL` |
| `icon` | `CharField` | Stores the icon | No | `star` | No | No | No | `-` | `-` |
| `color` | `CharField` | Stores the color | No | `#FFA500` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |

### Table: `gamification_studentachievement` (gamification.StudentAchievement)

- **Purpose:** Model representing `StudentAchievement` in the `gamification` app.
- **Real-world entity:** Represents a studentachievement entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `achievement` | `ForeignKey` | Stores the achievement | No | `-` | No | Yes | No | `Achievement` | `CASCADE` |
| `unlocked_at` | `DateTimeField` | Stores the unlocked at | No | `-` | No | No | No | `-` | `-` |

### Table: `attendance_attendancesession` (attendance.AttendanceSession)

- **Purpose:** Model representing `AttendanceSession` in the `attendance` app.
- **Real-world entity:** Represents a attendancesession entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `date` | `DateField` | Stores the date | No | `-` | No | Yes | No | `-` | `-` |
| `session_type` | `CharField` | Stores the session type | No | `full_day` | No | No | No | `-` | `-` |
| `notes` | `TextField` | General notes about the session | No | `-` | No | No | No | `-` | `-` |
| `is_finalized` | `BooleanField` | Once finalized, cannot be edited | No | `False` | No | No | No | `-` | `-` |
| `finalized_at` | `DateTimeField` | Stores the finalized at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `attendance_attendancerecord` (attendance.AttendanceRecord)

- **Purpose:** Model representing `AttendanceRecord` in the `attendance` app.
- **Real-world entity:** Represents a attendancerecord entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `session` | `ForeignKey` | Stores the session | No | `-` | No | Yes | No | `AttendanceSession` | `CASCADE` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `status` | `CharField` | Stores the status | No | `present` | No | Yes | No | `-` | `-` |
| `arrival_time` | `TimeField` | Stores the arrival time | Yes | `-` | No | No | No | `-` | `-` |
| `notes` | `TextField` | Specific notes for this student | No | `-` | No | No | No | `-` | `-` |
| `parent_notified` | `BooleanField` | Stores the parent notified | No | `False` | No | No | No | `-` | `-` |
| `parent_notified_at` | `DateTimeField` | Stores the parent notified at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `attendance_attendancestatistics` (attendance.AttendanceStatistics)

- **Purpose:** Model representing `AttendanceStatistics` in the `attendance` app.
- **Real-world entity:** Represents a attendancestatistics entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `OneToOneField` | Stores the student | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `total_sessions` | `PositiveIntegerField` | Stores the total sessions | No | `0` | No | No | No | `-` | `-` |
| `present_count` | `PositiveIntegerField` | Stores the present count | No | `0` | No | No | No | `-` | `-` |
| `absent_count` | `PositiveIntegerField` | Stores the absent count | No | `0` | No | No | No | `-` | `-` |
| `late_count` | `PositiveIntegerField` | Stores the late count | No | `0` | No | No | No | `-` | `-` |
| `excused_count` | `PositiveIntegerField` | Stores the excused count | No | `0` | No | No | No | `-` | `-` |
| `sick_count` | `PositiveIntegerField` | Stores the sick count | No | `0` | No | No | No | `-` | `-` |
| `attendance_percentage` | `DecimalField` | Stores the attendance percentage | No | `0` | No | No | No | `-` | `-` |
| `last_updated` | `DateTimeField` | Stores the last updated | No | `-` | No | No | No | `-` | `-` |

### Table: `performance_studentgrade` (performance.StudentGrade)

- **Purpose:** Model representing `StudentGrade` in the `performance` app.
- **Real-world entity:** Represents a studentgrade entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `academic_year` | `CharField` | e.g., 2025-2026 | No | `-` | No | No | No | `-` | `-` |
| `semester` | `CharField` | Stores the semester | No | `full_year` | No | No | No | `-` | `-` |
| `overall_percentage` | `DecimalField` | Stores the overall percentage | No | `0` | No | No | No | `-` | `-` |
| `overall_grade` | `CharField` | A+, A, B+, etc. | No | `-` | No | No | No | `-` | `-` |
| `gpa` | `DecimalField` | Grade Point Average | No | `0` | No | No | No | `-` | `-` |
| `class_rank` | `PositiveIntegerField` | Stores the class rank | Yes | `-` | No | No | No | `-` | `-` |
| `total_students` | `PositiveIntegerField` | Stores the total students | No | `0` | No | No | No | `-` | `-` |
| `attendance_percentage` | `DecimalField` | Stores the attendance percentage | No | `0` | No | No | No | `-` | `-` |
| `behavior_score` | `DecimalField` | Stores the behavior score | No | `100` | No | No | No | `-` | `-` |
| `is_passing` | `BooleanField` | Stores the is passing | No | `True` | No | No | No | `-` | `-` |
| `is_honor_roll` | `BooleanField` | Stores the is honor roll | No | `False` | No | No | No | `-` | `-` |
| `teacher_comments` | `TextField` | Stores the teacher comments | No | `-` | No | No | No | `-` | `-` |

### Table: `performance_subjectperformance` (performance.SubjectPerformance)

- **Purpose:** Model representing `SubjectPerformance` in the `performance` app.
- **Real-world entity:** Represents a subjectperformance entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `subject` | `ForeignKey` | Stores the subject | No | `-` | No | Yes | No | `Subject` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `academic_year` | `CharField` | Stores the academic year | No | `-` | No | No | No | `-` | `-` |
| `semester` | `CharField` | Stores the semester | No | `full_year` | No | No | No | `-` | `-` |
| `assignment_average` | `DecimalField` | Stores the assignment average | No | `0` | No | No | No | `-` | `-` |
| `quiz_average` | `DecimalField` | Stores the quiz average | No | `0` | No | No | No | `-` | `-` |
| `overall_score` | `DecimalField` | Stores the overall score | No | `0` | No | No | No | `-` | `-` |
| `letter_grade` | `CharField` | Stores the letter grade | No | `-` | No | No | No | `-` | `-` |
| `total_assignments` | `PositiveIntegerField` | Stores the total assignments | No | `0` | No | No | No | `-` | `-` |
| `completed_assignments` | `PositiveIntegerField` | Stores the completed assignments | No | `0` | No | No | No | `-` | `-` |
| `total_quizzes` | `PositiveIntegerField` | Stores the total quizzes | No | `0` | No | No | No | `-` | `-` |
| `completed_quizzes` | `PositiveIntegerField` | Stores the completed quizzes | No | `0` | No | No | No | `-` | `-` |
| `is_improving` | `BooleanField` | Stores the is improving | No | `False` | No | No | No | `-` | `-` |
| `trend` | `CharField` | Stores the trend | No | `stable` | No | No | No | `-` | `-` |
| `strengths` | `TextField` | Stores the strengths | No | `-` | No | No | No | `-` | `-` |
| `areas_for_improvement` | `TextField` | Stores the areas for improvement | No | `-` | No | No | No | `-` | `-` |

### Table: `performance_progressreport` (performance.ProgressReport)

- **Purpose:** Model representing `ProgressReport` in the `performance` app.
- **Real-world entity:** Represents a progressreport entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `report_type` | `CharField` | Stores the report type | No | `-` | No | No | No | `-` | `-` |
| `academic_year` | `CharField` | Stores the academic year | No | `-` | No | No | No | `-` | `-` |
| `report_period` | `CharField` | e.g., Q1, Semester 1 | No | `-` | No | No | No | `-` | `-` |
| `generated_at` | `DateTimeField` | Stores the generated at | No | `-` | No | No | No | `-` | `-` |
| `generated_by` | `ForeignKey` | Stores the generated by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `overall_performance` | `TextField` | Stores the overall performance | No | `-` | No | No | No | `-` | `-` |
| `academic_summary` | `TextField` | Stores the academic summary | No | `-` | No | No | No | `-` | `-` |
| `attendance_summary` | `TextField` | Stores the attendance summary | No | `-` | No | No | No | `-` | `-` |
| `behavior_summary` | `TextField` | Stores the behavior summary | No | `-` | No | No | No | `-` | `-` |
| `recommendations` | `TextField` | Stores the recommendations | No | `-` | No | No | No | `-` | `-` |
| `next_steps` | `TextField` | Stores the next steps | No | `-` | No | No | No | `-` | `-` |
| `pdf_file` | `FileField` | Stores the pdf file | Yes | `-` | No | No | No | `-` | `-` |
| `shared_with_parent` | `BooleanField` | Stores the shared with parent | No | `False` | No | No | No | `-` | `-` |
| `parent_viewed_at` | `DateTimeField` | Stores the parent viewed at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `performance_performancemetric` (performance.PerformanceMetric)

- **Purpose:** Model representing `PerformanceMetric` in the `performance` app.
- **Real-world entity:** Represents a performancemetric entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `metric_name` | `CharField` | Stores the metric name | No | `-` | No | No | No | `-` | `-` |
| `metric_type` | `CharField` | Stores the metric type | No | `-` | No | No | No | `-` | `-` |
| `current_value` | `DecimalField` | Stores the current value | No | `-` | No | No | No | `-` | `-` |
| `target_value` | `DecimalField` | Stores the target value | No | `-` | No | No | No | `-` | `-` |
| `unit` | `CharField` | %, points, count, etc. | No | `%` | No | No | No | `-` | `-` |
| `progress_percentage` | `DecimalField` | Stores the progress percentage | No | `0` | No | No | No | `-` | `-` |
| `is_achieved` | `BooleanField` | Stores the is achieved | No | `False` | No | No | No | `-` | `-` |
| `achieved_at` | `DateTimeField` | Stores the achieved at | Yes | `-` | No | No | No | `-` | `-` |
| `start_date` | `DateField` | Stores the start date | No | `-` | No | No | No | `-` | `-` |
| `target_date` | `DateField` | Stores the target date | No | `-` | No | No | No | `-` | `-` |
| `tracked_by` | `ForeignKey` | Stores the tracked by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `notes` | `TextField` | Stores the notes | No | `-` | No | No | No | `-` | `-` |

### Table: `communication_conversation` (communication.Conversation)

- **Purpose:** Model representing `Conversation` in the `communication` app.
- **Real-world entity:** Represents a conversation entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `conversation_type` | `CharField` | Stores the conversation type | No | `direct` | No | No | No | `-` | `-` |
| `title` | `CharField` | Required for group conversations | No | `-` | No | No | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `SET_NULL` |
| `created_by` | `ForeignKey` | Stores the created by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `last_message_at` | `DateTimeField` | Stores the last message at | No | `-` | No | Yes | No | `-` | `-` |
| `participants` | `ManyToManyField` | Stores the participants | No | `-` | No | No | No | `User` | `-` |

### Table: `communication_message` (communication.Message)

- **Purpose:** Model representing `Message` in the `communication` app.
- **Real-world entity:** Represents a message entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `conversation` | `ForeignKey` | Stores the conversation | No | `-` | No | Yes | No | `Conversation` | `CASCADE` |
| `sender` | `ForeignKey` | Stores the sender | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `message_text` | `TextField` | Stores the message text | No | `-` | No | No | No | `-` | `-` |
| `replied_to` | `ForeignKey` | Stores the replied to | Yes | `-` | No | Yes | No | `Message` | `SET_NULL` |
| `is_edited` | `BooleanField` | Stores the is edited | No | `False` | No | No | No | `-` | `-` |
| `edited_at` | `DateTimeField` | Stores the edited at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `communication_messageattachment` (communication.MessageAttachment)

- **Purpose:** Model representing `MessageAttachment` in the `communication` app.
- **Real-world entity:** Represents a messageattachment entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `message` | `ForeignKey` | Stores the message | No | `-` | No | Yes | No | `Message` | `CASCADE` |
| `file` | `FileField` | Stores the file | No | `-` | No | No | No | `-` | `-` |
| `file_name` | `CharField` | Stores the file name | No | `-` | No | No | No | `-` | `-` |
| `file_type` | `CharField` | Stores the file type | No | `-` | No | No | No | `-` | `-` |
| `file_size` | `PositiveIntegerField` | File size in bytes | No | `-` | No | No | No | `-` | `-` |
| `uploaded_by` | `ForeignKey` | Stores the uploaded by | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `download_count` | `PositiveIntegerField` | Stores the download count | No | `0` | No | No | No | `-` | `-` |

### Table: `communication_messageread` (communication.MessageRead)

- **Purpose:** Model representing `MessageRead` in the `communication` app.
- **Real-world entity:** Represents a messageread entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `message` | `ForeignKey` | Stores the message | No | `-` | No | Yes | No | `Message` | `CASCADE` |
| `user` | `ForeignKey` | Stores the user | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `read_at` | `DateTimeField` | Stores the read at | No | `-` | No | No | No | `-` | `-` |

### Table: `communication_announcement` (communication.Announcement)

- **Purpose:** Model representing `Announcement` in the `communication` app.
- **Real-world entity:** Represents a announcement entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | Yes | No | `-` | `-` |
| `content` | `TextField` | Stores the content | No | `-` | No | No | No | `-` | `-` |
| `sent_by` | `ForeignKey` | Stores the sent by | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `sent_at` | `DateTimeField` | Stores the sent at | Yes | `-` | No | Yes | No | `-` | `-` |
| `target_role` | `CharField` | Stores the target role | No | `-` | No | Yes | No | `-` | `-` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `scheduled_for` | `DateTimeField` | Schedule for future sending | Yes | `-` | No | No | No | `-` | `-` |
| `is_draft` | `BooleanField` | Stores the is draft | No | `False` | No | Yes | No | `-` | `-` |
| `priority` | `CharField` | Stores the priority | No | `normal` | No | Yes | No | `-` | `-` |
| `requires_acknowledgment` | `BooleanField` | Stores the requires acknowledgment | No | `False` | No | No | No | `-` | `-` |
| `total_recipients` | `PositiveIntegerField` | Stores the total recipients | No | `0` | No | No | No | `-` | `-` |
| `read_count` | `PositiveIntegerField` | Stores the read count | No | `0` | No | No | No | `-` | `-` |

### Table: `communication_announcementread` (communication.AnnouncementRead)

- **Purpose:** Model representing `AnnouncementRead` in the `communication` app.
- **Real-world entity:** Represents a announcementread entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `announcement` | `ForeignKey` | Stores the announcement | No | `-` | No | Yes | No | `Announcement` | `CASCADE` |
| `user` | `ForeignKey` | Stores the user | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `read_at` | `DateTimeField` | Stores the read at | Yes | `-` | No | No | No | `-` | `-` |
| `acknowledged_at` | `DateTimeField` | Stores the acknowledged at | Yes | `-` | No | No | No | `-` | `-` |

### Table: `behavior_behaviorincident` (behavior.BehaviorIncident)

- **Purpose:** Model representing `BehaviorIncident` in the `behavior` app.
- **Real-world entity:** Represents a behaviorincident entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `reported_by` | `ForeignKey` | Teacher/Admin who reported (null if AI-generated) | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `lecture` | `ForeignKey` | Lecture where incident occurred (if applicable) | Yes | `-` | No | Yes | No | `Lecture` | `SET_NULL` |
| `incident_type` | `CharField` | Stores the incident type | No | `-` | No | Yes | No | `-` | `-` |
| `severity` | `CharField` | Stores the severity | No | `minor` | No | Yes | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `incident_date` | `DateTimeField` | Stores the incident date | No | `<function now at 0x000001CC1B1C0C20>` | No | Yes | No | `-` | `-` |
| `source` | `CharField` | How this incident was created | No | `manual` | No | Yes | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | Yes | No | `-` | `-` |
| `ai_confidence_score` | `DecimalField` | AI confidence (0-100) if AI-generated | Yes | `-` | No | No | No | `-` | `-` |
| `ai_transcript_snippet` | `TextField` | Transcript excerpt that triggered AI detection | No | `-` | No | No | No | `-` | `-` |
| `lecture_timestamp` | `PositiveIntegerField` | Timestamp in lecture (seconds) where incident occurred | Yes | `-` | No | No | No | `-` | `-` |
| `student_notified` | `BooleanField` | Stores the student notified | No | `False` | No | No | No | `-` | `-` |
| `student_notified_at` | `DateTimeField` | Stores the student notified at | Yes | `-` | No | No | No | `-` | `-` |
| `parent_notified` | `BooleanField` | Stores the parent notified | No | `False` | No | No | No | `-` | `-` |
| `parent_notified_at` | `DateTimeField` | Stores the parent notified at | Yes | `-` | No | No | No | `-` | `-` |
| `requires_followup` | `BooleanField` | Stores the requires followup | No | `False` | No | No | No | `-` | `-` |
| `followup_notes` | `TextField` | Stores the followup notes | No | `-` | No | No | No | `-` | `-` |
| `resolved` | `BooleanField` | Stores the resolved | No | `False` | No | No | No | `-` | `-` |
| `resolved_at` | `DateTimeField` | Stores the resolved at | Yes | `-` | No | No | No | `-` | `-` |
| `resolved_by` | `ForeignKey` | Stores the resolved by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `behavior_behaviornote` (behavior.BehaviorNote)

- **Purpose:** Model representing `BehaviorNote` in the `behavior` app.
- **Real-world entity:** Represents a behaviornote entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `student` | `ForeignKey` | Stores the student | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `teacher` | `ForeignKey` | Stores the teacher | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `lecture` | `ForeignKey` | Stores the lecture | Yes | `-` | No | Yes | No | `Lecture` | `SET_NULL` |
| `note_type` | `CharField` | Stores the note type | No | `neutral` | No | Yes | No | `-` | `-` |
| `note` | `TextField` | Stores the note | No | `-` | No | No | No | `-` | `-` |
| `date` | `DateField` | Stores the date | No | `<function now at 0x000001CC1B1C0C20>` | No | Yes | No | `-` | `-` |
| `source` | `CharField` | Stores the source | No | `manual` | No | No | No | `-` | `-` |
| `is_ai_generated` | `BooleanField` | Stores the is ai generated | No | `False` | No | No | No | `-` | `-` |
| `ai_transcript_snippet` | `TextField` | Stores the ai transcript snippet | No | `-` | No | No | No | `-` | `-` |
| `lecture_timestamp` | `PositiveIntegerField` | Stores the lecture timestamp | Yes | `-` | No | No | No | `-` | `-` |
| `visible_to_student` | `BooleanField` | Stores the visible to student | No | `True` | No | No | No | `-` | `-` |
| `visible_to_parent` | `BooleanField` | Stores the visible to parent | No | `True` | No | No | No | `-` | `-` |

### Table: `behavior_behaviorstatistics` (behavior.BehaviorStatistics)

- **Purpose:** Model representing `BehaviorStatistics` in the `behavior` app.
- **Real-world entity:** Represents a behaviorstatistics entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `student` | `OneToOneField` | Stores the student | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | No | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `minor_incidents` | `PositiveIntegerField` | Stores the minor incidents | No | `0` | No | No | No | `-` | `-` |
| `moderate_incidents` | `PositiveIntegerField` | Stores the moderate incidents | No | `0` | No | No | No | `-` | `-` |
| `serious_incidents` | `PositiveIntegerField` | Stores the serious incidents | No | `0` | No | No | No | `-` | `-` |
| `critical_incidents` | `PositiveIntegerField` | Stores the critical incidents | No | `0` | No | No | No | `-` | `-` |
| `total_incidents` | `PositiveIntegerField` | Stores the total incidents | No | `0` | No | No | No | `-` | `-` |
| `ai_generated_incidents` | `PositiveIntegerField` | Stores the ai generated incidents | No | `0` | No | No | No | `-` | `-` |
| `manual_incidents` | `PositiveIntegerField` | Stores the manual incidents | No | `0` | No | No | No | `-` | `-` |
| `positive_notes` | `PositiveIntegerField` | Stores the positive notes | No | `0` | No | No | No | `-` | `-` |
| `neutral_notes` | `PositiveIntegerField` | Stores the neutral notes | No | `0` | No | No | No | `-` | `-` |
| `negative_notes` | `PositiveIntegerField` | Stores the negative notes | No | `0` | No | No | No | `-` | `-` |
| `total_notes` | `PositiveIntegerField` | Stores the total notes | No | `0` | No | No | No | `-` | `-` |
| `behavior_score` | `DecimalField` | 100 = perfect, decreases with incidents | No | `100` | No | No | No | `-` | `-` |
| `last_incident_date` | `DateTimeField` | Stores the last incident date | Yes | `-` | No | No | No | `-` | `-` |
| `last_updated` | `DateTimeField` | Stores the last updated | No | `-` | No | No | No | `-` | `-` |

### Table: `behavior_pendingbehaviordetection` (behavior.PendingBehaviorDetection)

- **Purpose:** Model representing `PendingBehaviorDetection` in the `behavior` app.
- **Real-world entity:** Represents a pendingbehaviordetection entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `lecture` | `ForeignKey` | Stores the lecture | No | `-` | No | Yes | No | `Lecture` | `CASCADE` |
| `student_name` | `CharField` | Student name extracted from transcript | No | `-` | No | No | No | `-` | `-` |
| `behavior_type` | `CharField` | Stores the behavior type | No | `-` | No | No | No | `-` | `-` |
| `severity` | `CharField` | Stores the severity | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | AI-generated neutral description | No | `-` | No | No | No | `-` | `-` |
| `original_statement` | `TextField` | Exact quote from lecture transcript | No | `-` | No | No | No | `-` | `-` |
| `is_positive` | `BooleanField` | Stores the is positive | No | `False` | No | No | No | `-` | `-` |
| `ai_confidence` | `CharField` | Stores the ai confidence | No | `MEDIUM` | No | No | No | `-` | `-` |
| `ai_confidence_score` | `DecimalField` | AI confidence (0-100) | No | `75.0` | No | No | No | `-` | `-` |
| `detection_sensitivity` | `CharField` | Sensitivity level used for detection | No | `MEDIUM` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `pending` | No | Yes | No | `-` | `-` |
| `reviewed_by` | `ForeignKey` | Stores the reviewed by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `reviewed_at` | `DateTimeField` | Stores the reviewed at | Yes | `-` | No | No | No | `-` | `-` |
| `teacher_notes` | `TextField` | Teacher comments or modifications | Yes | `-` | No | No | No | `-` | `-` |
| `modified_description` | `TextField` | Stores the modified description | Yes | `-` | No | No | No | `-` | `-` |
| `modified_severity` | `CharField` | Stores the modified severity | Yes | `-` | No | No | No | `-` | `-` |
| `modified_behavior_type` | `CharField` | Stores the modified behavior type | Yes | `-` | No | No | No | `-` | `-` |
| `student_notified` | `BooleanField` | Stores the student notified | No | `False` | No | No | No | `-` | `-` |
| `parent_notified` | `BooleanField` | Stores the parent notified | No | `False` | No | No | No | `-` | `-` |
| `notification_sent_at` | `DateTimeField` | Stores the notification sent at | Yes | `-` | No | No | No | `-` | `-` |
| `created_incident` | `ForeignKey` | Stores the created incident | Yes | `-` | No | Yes | No | `BehaviorIncident` | `SET_NULL` |
| `created_note` | `ForeignKey` | Stores the created note | Yes | `-` | No | Yes | No | `BehaviorNote` | `SET_NULL` |

### Table: `resources_resourcecategory` (resources.ResourceCategory)

- **Purpose:** Model representing `ResourceCategory` in the `resources` app.
- **Real-world entity:** Represents a resourcecategory entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `subject` | `ForeignKey` | Stores the subject | Yes | `-` | No | Yes | No | `Subject` | `CASCADE` |
| `grade_level` | `CharField` | Stores the grade level | No | `-` | No | No | No | `-` | `-` |
| `parent_category` | `ForeignKey` | Stores the parent category | Yes | `-` | No | Yes | No | `ResourceCategory` | `CASCADE` |
| `color` | `CharField` | Hex color code | No | `#3B82F6` | No | No | No | `-` | `-` |
| `icon` | `CharField` | Icon name/class | No | `-` | No | No | No | `-` | `-` |

### Table: `resources_resource` (resources.Resource)

- **Purpose:** Model representing `Resource` in the `resources` app.
- **Real-world entity:** Represents a resource entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `is_deleted` | `BooleanField` | Stores the is deleted | No | `False` | No | Yes | No | `-` | `-` |
| `deleted_at` | `DateTimeField` | Stores the deleted at | Yes | `-` | No | No | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | Yes | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `resource_type` | `CharField` | Stores the resource type | No | `file` | No | No | No | `-` | `-` |
| `file` | `FileField` | Stores the file | Yes | `-` | No | No | No | `-` | `-` |
| `external_link` | `CharField` | Stores the external link | No | `-` | No | No | No | `-` | `-` |
| `file_type` | `CharField` | Stores the file type | No | `-` | No | No | No | `-` | `-` |
| `file_size` | `PositiveIntegerField` | File size in bytes | No | `0` | No | No | No | `-` | `-` |
| `category` | `ForeignKey` | Stores the category | Yes | `-` | No | Yes | No | `ResourceCategory` | `SET_NULL` |
| `uploaded_by` | `ForeignKey` | Stores the uploaded by | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `subject` | `ForeignKey` | Stores the subject | Yes | `-` | No | Yes | No | `Subject` | `SET_NULL` |
| `grade_level` | `CharField` | Stores the grade level | No | `-` | No | No | No | `-` | `-` |
| `tags` | `CharField` | Comma-separated tags | No | `-` | No | No | No | `-` | `-` |
| `access_level` | `CharField` | Stores the access level | No | `public` | No | Yes | No | `-` | `-` |
| `download_count` | `PositiveIntegerField` | Stores the download count | No | `0` | No | No | No | `-` | `-` |
| `view_count` | `PositiveIntegerField` | Stores the view count | No | `0` | No | No | No | `-` | `-` |
| `thumbnail` | `FileField` | Stores the thumbnail | Yes | `-` | No | No | No | `-` | `-` |

### Table: `resources_resourcedownload` (resources.ResourceDownload)

- **Purpose:** Model representing `ResourceDownload` in the `resources` app.
- **Real-world entity:** Represents a resourcedownload entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `resource` | `ForeignKey` | Stores the resource | No | `-` | No | Yes | No | `Resource` | `CASCADE` |
| `user` | `ForeignKey` | Stores the user | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `downloaded_at` | `DateTimeField` | Stores the downloaded at | No | `-` | No | Yes | No | `-` | `-` |
| `ip_address` | `GenericIPAddressField` | Stores the ip address | Yes | `-` | No | No | No | `-` | `-` |

### Table: `notifications_notification` (notifications.Notification)

- **Purpose:** Model representing `Notification` in the `notifications` app.
- **Real-world entity:** Represents a notification entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `recipient` | `ForeignKey` | Stores the recipient | No | `-` | No | Yes | No | `User` | `CASCADE` |
| `notification_type` | `CharField` | Stores the notification type | No | `-` | No | Yes | No | `-` | `-` |
| `priority` | `CharField` | Stores the priority | No | `normal` | No | Yes | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `message` | `TextField` | Stores the message | No | `-` | No | No | No | `-` | `-` |
| `reference_type` | `CharField` | assignment, quiz, message, etc. | No | `-` | No | No | No | `-` | `-` |
| `reference_id` | `CharField` | Stores the reference id | No | `-` | No | No | No | `-` | `-` |
| `action_url` | `CharField` | URL to navigate to when clicked | No | `-` | No | No | No | `-` | `-` |
| `is_read` | `BooleanField` | Stores the is read | No | `False` | No | Yes | No | `-` | `-` |
| `read_at` | `DateTimeField` | Stores the read at | Yes | `-` | No | No | No | `-` | `-` |
| `sent_at` | `DateTimeField` | Stores the sent at | No | `-` | No | No | No | `-` | `-` |
| `metadata` | `JSONField` | Stores the metadata | No | `<class 'dict'>` | No | No | No | `-` | `-` |

### Table: `notifications_notificationpreference` (notifications.NotificationPreference)

- **Purpose:** Model representing `NotificationPreference` in the `notifications` app.
- **Real-world entity:** Represents a notificationpreference entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `user` | `OneToOneField` | Stores the user | No | `-` | Yes | Yes | No | `User` | `CASCADE` |
| `enable_in_app` | `BooleanField` | Stores the enable in app | No | `True` | No | No | No | `-` | `-` |
| `enable_email` | `BooleanField` | Stores the enable email | No | `True` | No | No | No | `-` | `-` |
| `email_frequency` | `CharField` | Stores the email frequency | No | `instant` | No | No | No | `-` | `-` |
| `enable_push` | `BooleanField` | Stores the enable push | No | `False` | No | No | No | `-` | `-` |
| `enable_sms` | `BooleanField` | Stores the enable sms | No | `False` | No | No | No | `-` | `-` |
| `notify_assignments` | `BooleanField` | Stores the notify assignments | No | `True` | No | No | No | `-` | `-` |
| `notify_quizzes` | `BooleanField` | Stores the notify quizzes | No | `True` | No | No | No | `-` | `-` |
| `notify_messages` | `BooleanField` | Stores the notify messages | No | `True` | No | No | No | `-` | `-` |
| `notify_announcements` | `BooleanField` | Stores the notify announcements | No | `True` | No | No | No | `-` | `-` |
| `notify_attendance` | `BooleanField` | Stores the notify attendance | No | `True` | No | No | No | `-` | `-` |
| `notify_behavior` | `BooleanField` | Stores the notify behavior | No | `True` | No | No | No | `-` | `-` |
| `notify_grades` | `BooleanField` | Stores the notify grades | No | `True` | No | No | No | `-` | `-` |
| `notify_gamification` | `BooleanField` | Stores the notify gamification | No | `True` | No | No | No | `-` | `-` |
| `notify_resources` | `BooleanField` | Stores the notify resources | No | `True` | No | No | No | `-` | `-` |
| `enable_quiet_hours` | `BooleanField` | Stores the enable quiet hours | No | `False` | No | No | No | `-` | `-` |
| `quiet_hours_start` | `TimeField` | e.g., 22:00 | Yes | `-` | No | No | No | `-` | `-` |
| `quiet_hours_end` | `TimeField` | e.g., 07:00 | Yes | `-` | No | No | No | `-` | `-` |

### Table: `notifications_notificationtemplate` (notifications.NotificationTemplate)

- **Purpose:** Model representing `NotificationTemplate` in the `notifications` app.
- **Real-world entity:** Represents a notificationtemplate entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | Yes | No | No | `-` | `-` |
| `notification_type` | `CharField` | Stores the notification type | No | `-` | No | No | No | `-` | `-` |
| `title_template` | `CharField` | Use {variable} for placeholders | No | `-` | No | No | No | `-` | `-` |
| `message_template` | `TextField` | Use {variable} for placeholders | No | `-` | No | No | No | `-` | `-` |
| `email_subject_template` | `CharField` | Stores the email subject template | No | `-` | No | No | No | `-` | `-` |
| `email_body_template` | `TextField` | Stores the email body template | No | `-` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |
| `priority` | `CharField` | Stores the priority | No | `normal` | No | No | No | `-` | `-` |

### Table: `notifications_notificationbatch` (notifications.NotificationBatch)

- **Purpose:** Model representing `NotificationBatch` in the `notifications` app.
- **Real-world entity:** Represents a notificationbatch entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `notification_type` | `CharField` | Stores the notification type | No | `-` | No | No | No | `-` | `-` |
| `title` | `CharField` | Stores the title | No | `-` | No | No | No | `-` | `-` |
| `message` | `TextField` | Stores the message | No | `-` | No | No | No | `-` | `-` |
| `recipient_count` | `PositiveIntegerField` | Stores the recipient count | No | `0` | No | No | No | `-` | `-` |
| `sent_count` | `PositiveIntegerField` | Stores the sent count | No | `0` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `pending` | No | No | No | `-` | `-` |
| `scheduled_for` | `DateTimeField` | Stores the scheduled for | Yes | `-` | No | No | No | `-` | `-` |
| `sent_at` | `DateTimeField` | Stores the sent at | Yes | `-` | No | No | No | `-` | `-` |
| `created_by` | `ForeignKey` | Stores the created by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `reports_reporttemplate` (reports.ReportTemplate)

- **Purpose:** Model representing `ReportTemplate` in the `reports` app.
- **Real-world entity:** Represents a reporttemplate entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | Yes | No | No | `-` | `-` |
| `description` | `TextField` | Stores the description | No | `-` | No | No | No | `-` | `-` |
| `report_type` | `CharField` | Stores the report type | No | `-` | No | Yes | No | `-` | `-` |
| `sections` | `JSONField` | Sections to include: grades, attendance, behavior, etc. | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `layout_config` | `JSONField` | Layout settings: colors, fonts, logo, etc. | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |
| `is_default` | `BooleanField` | Stores the is default | No | `False` | No | No | No | `-` | `-` |
| `created_by` | `ForeignKey` | Stores the created by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `reports_report` (reports.Report)

- **Purpose:** Model representing `Report` in the `reports` app.
- **Real-world entity:** Represents a report entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `report_type` | `CharField` | Stores the report type | No | `-` | No | Yes | No | `-` | `-` |
| `template` | `ForeignKey` | Stores the template | Yes | `-` | No | Yes | No | `ReportTemplate` | `SET_NULL` |
| `student` | `ForeignKey` | Stores the student | Yes | `-` | No | Yes | No | `User` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `parameters` | `JSONField` | Filters: academic_year, semester, date_range, etc. | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `file_format` | `CharField` | Stores the file format | No | `pdf` | No | No | No | `-` | `-` |
| `file` | `FileField` | Stores the file | Yes | `-` | No | No | No | `-` | `-` |
| `file_size` | `PositiveIntegerField` | File size in bytes | No | `0` | No | No | No | `-` | `-` |
| `status` | `CharField` | Stores the status | No | `pending` | No | Yes | No | `-` | `-` |
| `error_message` | `TextField` | Stores the error message | No | `-` | No | No | No | `-` | `-` |
| `generated_by` | `ForeignKey` | Stores the generated by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `generated_at` | `DateTimeField` | Stores the generated at | Yes | `-` | No | No | No | `-` | `-` |
| `is_scheduled` | `BooleanField` | Stores the is scheduled | No | `False` | No | No | No | `-` | `-` |
| `schedule` | `ForeignKey` | Stores the schedule | Yes | `-` | No | Yes | No | `ReportSchedule` | `SET_NULL` |
| `is_shared` | `BooleanField` | Stores the is shared | No | `False` | No | No | No | `-` | `-` |
| `shared_with` | `ManyToManyField` | Stores the shared with | No | `-` | No | No | No | `User` | `-` |

### Table: `reports_reportschedule` (reports.ReportSchedule)

- **Purpose:** Model representing `ReportSchedule` in the `reports` app.
- **Real-world entity:** Represents a reportschedule entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `template` | `ForeignKey` | Stores the template | No | `-` | No | Yes | No | `ReportTemplate` | `CASCADE` |
| `classroom` | `ForeignKey` | Stores the classroom | Yes | `-` | No | Yes | No | `Classroom` | `CASCADE` |
| `frequency` | `CharField` | Stores the frequency | No | `-` | No | No | No | `-` | `-` |
| `next_run_date` | `DateTimeField` | Stores the next run date | No | `-` | No | Yes | No | `-` | `-` |
| `last_run_date` | `DateTimeField` | Stores the last run date | Yes | `-` | No | No | No | `-` | `-` |
| `recipients` | `JSONField` | List of email addresses to send report to | No | `<class 'list'>` | No | No | No | `-` | `-` |
| `is_active` | `BooleanField` | Stores the is active | No | `True` | No | No | No | `-` | `-` |
| `created_by` | `ForeignKey` | Stores the created by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |

### Table: `reports_dataexport` (reports.DataExport)

- **Purpose:** Model representing `DataExport` in the `reports` app.
- **Real-world entity:** Represents a dataexport entity.
- **Type:** Supporting table

#### Columns

| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |
|---|---|---|---|---|---|---|---|---|---|
| `id` | `UUIDField` | Stores the id | No | `<function uuid4 at 0x000001CC1B438040>` | Yes | No | Yes | `-` | `-` |
| `created_at` | `DateTimeField` | Stores the created at | No | `-` | No | Yes | No | `-` | `-` |
| `updated_at` | `DateTimeField` | Stores the updated at | No | `-` | No | No | No | `-` | `-` |
| `export_type` | `CharField` | Stores the export type | No | `-` | No | Yes | No | `-` | `-` |
| `name` | `CharField` | Stores the name | No | `-` | No | No | No | `-` | `-` |
| `filters` | `JSONField` | Filters: classroom, date_range, students, etc. | No | `<class 'dict'>` | No | No | No | `-` | `-` |
| `file_format` | `CharField` | Stores the file format | No | `excel` | No | No | No | `-` | `-` |
| `file` | `FileField` | Stores the file | Yes | `-` | No | No | No | `-` | `-` |
| `file_size` | `PositiveIntegerField` | Stores the file size | No | `0` | No | No | No | `-` | `-` |
| `row_count` | `PositiveIntegerField` | Number of rows exported | No | `0` | No | No | No | `-` | `-` |
| `exported_by` | `ForeignKey` | Stores the exported by | Yes | `-` | No | Yes | No | `User` | `SET_NULL` |
| `exported_at` | `DateTimeField` | Stores the exported at | No | `-` | No | No | No | `-` | `-` |

## PART 3 — Relationships

### Foreign Key (One-to-Many / Many-to-One) Relationships

#### One-to-Many
- `AcademicYear` (1) ---- (Many) `Classroom` (via `academic_year`)
- `Achievement` (1) ---- (Many) `StudentAchievement` (via `achievement`)
- `Announcement` (1) ---- (Many) `AnnouncementRead` (via `announcement`)
- `AssignmentGrade` (1) ---- (Many) `GradingAuditLog` (via `grade`)
- `AssignmentGrade` (1) ---- (Many) `RubricScore` (via `grade`)
- `Assignment` (1) ---- (Many) `AssignmentQuestion` (via `assignment`)
- `Assignment` (1) ---- (Many) `AssignmentSubmission` (via `assignment`)
- `Assignment` (1) ---- (Many) `RubricCriterion` (via `assignment`)
- `AttendanceSession` (1) ---- (Many) `AttendanceRecord` (via `session`)
- `Badge` (1) ---- (Many) `Achievement` (via `badge_reward`)
- `Badge` (1) ---- (Many) `StudentBadge` (via `badge`)
- `BehaviorIncident` (1) ---- (Many) `PendingBehaviorDetection` (via `created_incident`)
- `BehaviorNote` (1) ---- (Many) `PendingBehaviorDetection` (via `created_note`)
- `Classroom` (1) ---- (Many) `Announcement` (via `classroom`)
- `Classroom` (1) ---- (Many) `Assignment` (via `classroom`)
- `Classroom` (1) ---- (Many) `AttendanceSession` (via `classroom`)
- `Classroom` (1) ---- (Many) `AttendanceStatistics` (via `classroom`)
- `Classroom` (1) ---- (Many) `BehaviorIncident` (via `classroom`)
- `Classroom` (1) ---- (Many) `BehaviorNote` (via `classroom`)
- `Classroom` (1) ---- (Many) `BehaviorStatistics` (via `classroom`)
- `Classroom` (1) ---- (Many) `ClassroomEnrollment` (via `classroom`)
- `Classroom` (1) ---- (Many) `Conversation` (via `classroom`)
- `Classroom` (1) ---- (Many) `FlashcardSet` (via `classroom`)
- `Classroom` (1) ---- (Many) `Leaderboard` (via `classroom`)
- `Classroom` (1) ---- (Many) `LectureGame` (via `classroom`)
- `Classroom` (1) ---- (Many) `LectureNote` (via `classroom`)
- `Classroom` (1) ---- (Many) `Lecture` (via `classroom`)
- `Classroom` (1) ---- (Many) `ProgressReport` (via `classroom`)
- `Classroom` (1) ---- (Many) `Quiz` (via `classroom`)
- `Classroom` (1) ---- (Many) `ReportSchedule` (via `classroom`)
- `Classroom` (1) ---- (Many) `Report` (via `classroom`)
- `Classroom` (1) ---- (Many) `Resource` (via `classroom`)
- `Classroom` (1) ---- (Many) `StudentGrade` (via `classroom`)
- `Classroom` (1) ---- (Many) `SubjectPerformance` (via `classroom`)
- `Conversation` (1) ---- (Many) `Message` (via `conversation`)
- `FlashcardSet` (1) ---- (Many) `Flashcard` (via `flashcard_set`)
- `FlashcardSet` (1) ---- (Many) `StudentFlashcardSetView` (via `flashcard_set`)
- `Flashcard` (1) ---- (Many) `StudentFlashcardProgress` (via `flashcard`)
- `GameAttempt` (1) ---- (Many) `GameLeaderboard` (via `best_attempt`)
- `GameTemplate` (1) ---- (Many) `LectureGame` (via `template`)
- `Leaderboard` (1) ---- (Many) `LeaderboardEntry` (via `leaderboard`)
- `LectureGame` (1) ---- (Many) `GameAttempt` (via `lecture_game`)
- `LectureGame` (1) ---- (Many) `GameLeaderboard` (via `lecture_game`)
- `LectureNote` (1) ---- (Many) `StudentNoteBookmark` (via `note`)
- `LectureNote` (1) ---- (Many) `StudentNoteView` (via `note`)
- `LectureNote` (1) ---- (Many) `StudentPersonalNote` (via `lecture_note`)
- `Lecture` (1) ---- (Many) `Assignment` (via `source_lecture`)
- `Lecture` (1) ---- (Many) `BehaviorIncident` (via `lecture`)
- `Lecture` (1) ---- (Many) `BehaviorNote` (via `lecture`)
- `Lecture` (1) ---- (Many) `FlashcardSet` (via `lecture`)
- `Lecture` (1) ---- (Many) `LectureBookmark` (via `lecture`)
- `Lecture` (1) ---- (Many) `LectureGame` (via `lecture`)
- `Lecture` (1) ---- (Many) `LectureResource` (via `lecture`)
- `Lecture` (1) ---- (Many) `LectureView` (via `lecture`)
- `Lecture` (1) ---- (Many) `PendingBehaviorDetection` (via `lecture`)
- `Message` (1) ---- (Many) `MessageAttachment` (via `message`)
- `Message` (1) ---- (Many) `MessageRead` (via `message`)
- `Message` (1) ---- (Many) `Message` (via `replied_to`)
- `NoteTemplate` (1) ---- (Many) `LectureNote` (via `template`)
- `QuestionOption` (1) ---- (Many) `QuizAnswer` (via `selected_option`)
- `Question` (1) ---- (Many) `QuestionOption` (via `question`)
- `Question` (1) ---- (Many) `QuizAnswer` (via `question`)
- `QuizAttempt` (1) ---- (Many) `QuizAnswer` (via `attempt`)
- `Quiz` (1) ---- (Many) `Question` (via `quiz`)
- `Quiz` (1) ---- (Many) `QuizAttempt` (via `quiz`)
- `ReportSchedule` (1) ---- (Many) `Report` (via `schedule`)
- `ReportTemplate` (1) ---- (Many) `ReportSchedule` (via `template`)
- `ReportTemplate` (1) ---- (Many) `Report` (via `template`)
- `ResourceCategory` (1) ---- (Many) `ResourceCategory` (via `parent_category`)
- `ResourceCategory` (1) ---- (Many) `Resource` (via `category`)
- `Resource` (1) ---- (Many) `ResourceDownload` (via `resource`)
- `RubricCriterion` (1) ---- (Many) `RubricScore` (via `criterion`)
- `School` (1) ---- (Many) `AcademicYear` (via `school`)
- `School` (1) ---- (Many) `Classroom` (via `school`)
- `Subject` (1) ---- (Many) `Classroom` (via `subject`)
- `Subject` (1) ---- (Many) `ResourceCategory` (via `subject`)
- `Subject` (1) ---- (Many) `Resource` (via `subject`)
- `Subject` (1) ---- (Many) `SubjectPerformance` (via `subject`)
- `User` (1) ---- (Many) `AnnouncementRead` (via `user`)
- `User` (1) ---- (Many) `Announcement` (via `sent_by`)
- `User` (1) ---- (Many) `AssignmentGrade` (via `graded_by`)
- `User` (1) ---- (Many) `AssignmentSubmission` (via `student`)
- `User` (1) ---- (Many) `Assignment` (via `created_by`)
- `User` (1) ---- (Many) `AttendanceRecord` (via `student`)
- `User` (1) ---- (Many) `AttendanceSession` (via `teacher`)
- `User` (1) ---- (Many) `BehaviorIncident` (via `reported_by`)
- `User` (1) ---- (Many) `BehaviorIncident` (via `resolved_by`)
- `User` (1) ---- (Many) `BehaviorIncident` (via `student`)
- `User` (1) ---- (Many) `BehaviorNote` (via `student`)
- `User` (1) ---- (Many) `BehaviorNote` (via `teacher`)
- `User` (1) ---- (Many) `ClassroomEnrollment` (via `student`)
- `User` (1) ---- (Many) `Classroom` (via `teacher`)
- `User` (1) ---- (Many) `Conversation` (via `created_by`)
- `User` (1) ---- (Many) `DataExport` (via `exported_by`)
- `User` (1) ---- (Many) `FlashcardSet` (via `teacher`)
- `User` (1) ---- (Many) `GameAttempt` (via `student`)
- `User` (1) ---- (Many) `GameLeaderboard` (via `student`)
- `User` (1) ---- (Many) `GradingAuditLog` (via `performed_by`)
- `User` (1) ---- (Many) `LeaderboardEntry` (via `student`)
- `User` (1) ---- (Many) `LectureBookmark` (via `created_by`)
- `User` (1) ---- (Many) `LectureGame` (via `generated_by`)
- `User` (1) ---- (Many) `LectureGame` (via `highest_scorer`)
- `User` (1) ---- (Many) `LectureGame` (via `published_by`)
- `User` (1) ---- (Many) `LectureNote` (via `teacher`)
- `User` (1) ---- (Many) `LectureView` (via `student`)
- `User` (1) ---- (Many) `Lecture` (via `teacher`)
- `User` (1) ---- (Many) `MessageAttachment` (via `uploaded_by`)
- `User` (1) ---- (Many) `MessageRead` (via `user`)
- `User` (1) ---- (Many) `Message` (via `sender`)
- `User` (1) ---- (Many) `NoteTemplate` (via `created_by`)
- `User` (1) ---- (Many) `NotificationBatch` (via `created_by`)
- `User` (1) ---- (Many) `Notification` (via `recipient`)
- `User` (1) ---- (Many) `ParentStudentRelationship` (via `parent`)
- `User` (1) ---- (Many) `ParentStudentRelationship` (via `student`)
- `User` (1) ---- (Many) `PendingBehaviorDetection` (via `reviewed_by`)
- `User` (1) ---- (Many) `PerformanceMetric` (via `student`)
- `User` (1) ---- (Many) `PerformanceMetric` (via `tracked_by`)
- `User` (1) ---- (Many) `ProgressReport` (via `generated_by`)
- `User` (1) ---- (Many) `ProgressReport` (via `student`)
- `User` (1) ---- (Many) `QuizAttempt` (via `student`)
- `User` (1) ---- (Many) `Quiz` (via `teacher`)
- `User` (1) ---- (Many) `ReportSchedule` (via `created_by`)
- `User` (1) ---- (Many) `ReportTemplate` (via `created_by`)
- `User` (1) ---- (Many) `Report` (via `generated_by`)
- `User` (1) ---- (Many) `Report` (via `student`)
- `User` (1) ---- (Many) `ResourceDownload` (via `user`)
- `User` (1) ---- (Many) `Resource` (via `uploaded_by`)
- `User` (1) ---- (Many) `StudentAchievement` (via `student`)
- `User` (1) ---- (Many) `StudentBadge` (via `student`)
- `User` (1) ---- (Many) `StudentFlashcardProgress` (via `student`)
- `User` (1) ---- (Many) `StudentFlashcardSetView` (via `student`)
- `User` (1) ---- (Many) `StudentGrade` (via `student`)
- `User` (1) ---- (Many) `StudentNoteBookmark` (via `student`)
- `User` (1) ---- (Many) `StudentNoteView` (via `student`)
- `User` (1) ---- (Many) `StudentPersonalNote` (via `student`)
- `User` (1) ---- (Many) `SubjectPerformance` (via `student`)
- `User` (1) ---- (Many) `XPTransaction` (via `awarded_by`)
- `User` (1) ---- (Many) `XPTransaction` (via `student`)

#### Many-to-Many
- `Conversation` (Many) <--> (Many) `User` (via `participants`)
- `Report` (Many) <--> (Many) `User` (via `shared_with`)
- `User` (Many) <--> (Many) `Group` (via `groups`)
- `User` (Many) <--> (Many) `Permission` (via `user_permissions`)

#### One-to-One
- `AssignmentGrade` (1) <--> (1) `AssignmentSubmission` (via `submission`)
- `AttendanceStatistics` (1) <--> (1) `User` (via `student`)
- `BehaviorStatistics` (1) <--> (1) `User` (via `student`)
- `LectureNote` (1) <--> (1) `Lecture` (via `lecture`)
- `NotificationPreference` (1) <--> (1) `User` (via `user`)
- `ParentProfile` (1) <--> (1) `User` (via `user`)
- `StudentProfile` (1) <--> (1) `User` (via `user`)
- `StudentXP` (1) <--> (1) `User` (via `student`)
- `TeacherProfile` (1) <--> (1) `User` (via `user`)

#### Self-Referencing Tables
- `Message` references itself via `replied_to`
- `ResourceCategory` references itself via `parent_category`

### ER Diagram (Text-Based Highlights)

```text
User (1) ------ (1) StudentProfile / TeacherProfile / ParentProfile
School (1) ---- (Many) User (Teachers/Students)
School (1) ---- (Many) ClassRoom
Teacher (1) --- (Many) ClassRoom (via class_teacher)
ClassRoom (1) - (Many) Enrollment ---- (1) Student
ClassRoom (1) - (Many) Subject
Teacher (1) --- (Many) Subject
Subject (1) --- (Many) Assignment / Assessment / Lecture
Student (1) --- (Many) Submission / Grade / Attendance
```

## PART 4 — Keys & Constraints

### Composite Keys / Unique Together Constraints
- `ParentStudentRelationship`: ["('parent', 'student')"]
- `AcademicYear`: ["('school', 'name')"]
- `Subject`: ["('name', 'grade')"]
- `Classroom`: ["('school', 'academic_year', 'subject', 'grade', 'section')"]
- `ClassroomEnrollment`: ["('classroom', 'student')"]
- `LectureView`: ["('lecture', 'student')"]
- `StudentNoteBookmark`: ["('note', 'student')"]
- `StudentNoteView`: ["('note', 'student')"]
- `StudentFlashcardProgress`: ["('flashcard', 'student')"]
- `StudentFlashcardSetView`: ["('flashcard_set', 'student')"]
- `LectureGame`: ["('lecture', 'template', 'difficulty')"]
- `GameLeaderboard`: ["('lecture_game', 'student')"]
- `AssignmentQuestion`: ["('assignment', 'question_number')"]
- `AssignmentSubmission`: ["('assignment', 'student')"]
- `RubricScore`: ["('grade', 'criterion')"]
- `QuizAnswer`: ["('attempt', 'question')"]
- `StudentBadge`: ["('student', 'badge')"]
- `LeaderboardEntry`: ["('leaderboard', 'student')"]
- `StudentAchievement`: ["('student', 'achievement')"]
- `AttendanceSession`: ["('classroom', 'date', 'session_type')"]
- `AttendanceRecord`: ["('session', 'student')"]
- `AttendanceStatistics`: ["('student', 'classroom')"]
- `StudentGrade`: ["('student', 'classroom', 'academic_year', 'semester')"]
- `SubjectPerformance`: ["('student', 'subject', 'classroom', 'academic_year', 'semester')"]
- `MessageRead`: ["('message', 'user')"]
- `AnnouncementRead`: ["('announcement', 'user')"]
- `BehaviorStatistics`: ["('student', 'classroom')"]

### Model-Level Constraints

### System Constraints Rules
- **Primary Keys:** Every table has a surrogate `id` (BigAutoField) unless overridden.
- **Foreign Keys:** Enforce referential integrity, preventing orphans for core entities (mostly via CASCADE).
- **NOT NULL:** Enforced on all non-nullable database columns (see Tables section).

## PART 5 — Data Flow Understanding

### When a new teacher is created:
1. A new record is inserted into the `User` (`accounts_user`) table with `role='teacher'`.
2. A linked record is inserted into `TeacherProfile` (`accounts_teacherprofile`) storing teacher-specific metadata.
3. Depending on assignments, they may be linked to `Subject` or `ClassRoom` records.

### When a student enrolls:
1. The student exists in `User` and `StudentProfile`.
2. An `Enrollment` record is created linking the `StudentProfile` (or `User`) to a specific `ClassRoom` and `AcademicYear`.
3. This cascades into access rights: the student can now view `Assignment`, `Lecture`, and submit `Submission` records tied to that `ClassRoom`'s `Subject`s.

### When a teacher is deleted:
1. `User.is_deleted = True` or the record is CASCADE deleted, depending on soft delete settings.
2. If hard deleted, `TeacherProfile` is CASCADE deleted.
3. Their linked `Subject`s and `ClassRoom.class_teacher` references might be SET_NULL or restricted to prevent deleting the whole class.

### If a parent record is deleted:
1. If an `AcademicYear` is deleted, all `Enrollment`s might be CASCADE deleted.
2. If a `ClassRoom` is deleted, its `Enrollment`s, `Subject`s, and `Assignment`s usually CASCADE, wiping out a huge branch of data. Standard models use `is_deleted` (Soft Delete) to prevent this catastrophic data loss.

## PART 6 — Things I Must Be Careful About Before Editing

### Central and Risky Tables:
- **`User` / `StudentProfile` / `TeacherProfile`:** The root of identity and authentication. Editing these requires extreme care around `AUTH_USER_MODEL` and foreign keys.
- **`ClassRoom` / `Subject` / `Enrollment`:** The organizational backbone. All academic data flows from these. Breaking an enrollment breaks a student's entire view.
- **`AcademicYear`:** Time-based scoping. Messing with this cascades into historical views for all users.

### Circular Dependencies & Risks:
- Modifying `User` -> `Profile` (OneToOne) usually requires updating both atomically.
- Be careful with `is_deleted` soft-deletes. Uniqueness constraints often clash with soft-deleted records (e.g., creating a new user with an email that was 'deleted'). You may need to build unique constraints that only apply `WHERE is_deleted=FALSE`.
- **Cascades:** Many FKs use `CASCADE`. Deleting a `School` or `ClassRoom` record directly from the DB will mercilessly wipe out assignments, submissions, and grades. USE SOFT DELETE OR UPDATE `is_active=False` INSTEAD of raw `DELETE` statements.
