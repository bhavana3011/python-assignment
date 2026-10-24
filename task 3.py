
# University Academic Progression Audit

name = input("Enter student name: ")
semester = int(input("Enter current semester: "))
subjects = int(input("Enter number of subjects: "))
pass_mark = 10
minimum_attendance = 75
passed_subjects = 0
failed_subjects = []

for i in range(1, subjects + 1):
    subject = input(f"Enter subject {i} name: ")
    marks = float(input(f"Enter marks in {subject}: "))

    if marks >= pass_mark:
        passed_subjects += 1
    else:
        failed_subjects.append(subject)

# Check attendance
attendance = float(input("Enter attendance percentage: "))

# Check prerequisite completion
prerequisite = input(
    "Are all prerequisites completed? (yes/no): "
).lower()

# Display audit report
print("\n--- Academic Progression Audit ---")
print("Student Name:", name)
print("Current Semester:", semester)
print("Subjects Passed:", passed_subjects, "/", subjects)
print("Attendance:", attendance, "%")

if failed_subjects:
    print("Failed Subjects:", ", ".join(failed_subjects))
else:
    print("Failed Subjects: None")

if attendance < minimum_attendance:
    print("Requirement Pending: Minimum attendance not met")

if prerequisite != "yes":
    print("Requirement Pending: Prerequisites not completed")

if passed_subjects == subjects and attendance >= minimum_attendance and prerequisite == "yes":
    print("Result: Eligible for next semester")
else:
    print("Result: Not eligible for next semester")
    print("Please complete the outstanding requirements.")
