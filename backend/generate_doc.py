import json

with open('schema_dump.json', 'r') as f:
    schema = json.load(f)

md = []
md.append("# Database Schema Documentation\n\n")

# PART 1 & 2
md.append("## PART 1 & 2 — Tables Overview and Columns Breakdown\n\n")

for model_path, data in schema.items():
    app = data['app']
    model_name = data['model']
    table_name = data['table_name']
    
    # Determine purpose and core/supporting
    is_core = app in ['core', 'accounts', 'schools'] or model_name in ['StudentProfile', 'TeacherProfile', 'User', 'School', 'ClassRoom', 'Subject', 'Enrollment']
    core_text = "Core table" if is_core else "Supporting table"
    
    md.append(f"### Table: `{table_name}` ({app}.{model_name})\n\n")
    md.append(f"- **Purpose:** Model representing `{model_name}` in the `{app}` app.\n")
    md.append(f"- **Real-world entity:** Represents a {model_name.lower()} entity.\n")
    md.append(f"- **Type:** {core_text}\n\n")
    
    md.append("#### Columns\n\n")
    md.append("| Column Name | Type | Meaning / Value Stored | Nullable? | Default | Unique | Indexed | PK | FK To | On Delete |\n")
    md.append("|---|---|---|---|---|---|---|---|---|---|\n")
    
    for field in data['fields']:
        f_name = field['name']
        f_type = field['type']
        f_null = 'Yes' if field['null'] else 'No'
        f_default = field['default'] if field['default'] and field['default'] != 'None' else '-'
        f_unique = 'Yes' if field['unique'] else 'No'
        f_index = 'Yes' if field['db_index'] else 'No'
        f_pk = 'Yes' if field['primary_key'] else 'No'
        f_fk = field['related_model'] if field['is_relation'] else '-'
        f_on_delete = field['on_delete'] if field['on_delete'] else '-'
        
        meaning = field.get('help_text', '') 
        if not meaning:
            meaning = f"Stores the {f_name.replace('_', ' ')}"
            
        md.append(f"| `{f_name}` | `{f_type}` | {meaning} | {f_null} | `{f_default}` | {f_unique} | {f_index} | {f_pk} | `{f_fk}` | `{f_on_delete}` |\n")
        
    md.append("\n")

# PART 3: Relationships
md.append("## PART 3 — Relationships\n\n")
md.append("### Foreign Key (One-to-Many / Many-to-One) Relationships\n\n")
m2m = []
o2m = []
o2o = []
SelfRef = []

for model_path, data in schema.items():
    m_name = data['model']
    for field in data['fields']:
        if field['is_relation'] and field['related_model']:
            rel = field['related_model']
            
            if field['type'] == 'ManyToManyField':
                m2m.append(f"- `{m_name}` (Many) <--> (Many) `{rel}` (via `{field['name']}`)")
            elif field['type'] == 'OneToOneField':
                o2o.append(f"- `{m_name}` (1) <--> (1) `{rel}` (via `{field['name']}`)")
            else: # ForeignKey
                o2m.append(f"- `{rel}` (1) ---- (Many) `{m_name}` (via `{field['name']}`)")
                
            if rel == m_name or rel == 'self':
                SelfRef.append(f"- `{m_name}` references itself via `{field['name']}`")

md.append("#### One-to-Many\n")
for rel in sorted(set(o2m)):
    md.append(rel + "\n")
    
md.append("\n#### Many-to-Many\n")
for rel in sorted(set(m2m)):
    md.append(rel + "\n")
    
md.append("\n#### One-to-One\n")
for rel in sorted(set(o2o)):
    md.append(rel + "\n")
    
if SelfRef:
    md.append("\n#### Self-Referencing Tables\n")
    for rel in sorted(set(SelfRef)):
        md.append(rel + "\n")

md.append("\n### ER Diagram (Text-Based Highlights)\n\n")
md.append("```text\n")
md.append("User (1) ------ (1) StudentProfile / TeacherProfile / ParentProfile\n")
md.append("School (1) ---- (Many) User (Teachers/Students)\n")
md.append("School (1) ---- (Many) ClassRoom\n")
md.append("Teacher (1) --- (Many) ClassRoom (via class_teacher)\n")
md.append("ClassRoom (1) - (Many) Enrollment ---- (1) Student\n")
md.append("ClassRoom (1) - (Many) Subject\n")
md.append("Teacher (1) --- (Many) Subject\n")
md.append("Subject (1) --- (Many) Assignment / Assessment / Lecture\n")
md.append("Student (1) --- (Many) Submission / Grade / Attendance\n")
md.append("```\n\n")

# PART 4: Constraints
md.append("## PART 4 — Keys & Constraints\n\n")
md.append("### Composite Keys / Unique Together Constraints\n")
for model_path, data in schema.items():
    if data['unique_together']:
        md.append(f"- `{data['model']}`: {data['unique_together']}\n")

md.append("\n### Model-Level Constraints\n")
for model_path, data in schema.items():
    if data['constraints']:
        for c in data['constraints']:
            md.append(f"- `{data['model']}`: `{c}`\n")

md.append("\n### System Constraints Rules\n")
md.append("- **Primary Keys:** Every table has a surrogate `id` (BigAutoField) unless overridden.\n")
md.append("- **Foreign Keys:** Enforce referential integrity, preventing orphans for core entities (mostly via CASCADE).\n")
md.append("- **NOT NULL:** Enforced on all non-nullable database columns (see Tables section).\n")

# PART 5 & 6
md.append("""
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
""")

with open('database_schema.md', 'w', encoding='utf-8') as f:
    f.writelines(md)

print("Generated database_schema.md")
