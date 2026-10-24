
# Smart Classroom Timetable Allocation

# Course details: (course name, students, period)
courses = [
    ("Python", 40, "9 AM"),
    ("Maths", 30, "10 AM"),
    ("English", 50, "9 AM"),
    ("Physics", 25, "11 AM")
]

# Room details: (room name, capacity)
rooms = [
    ("Room 101", 45),
    ("Room 102", 35)
]

allocated = []
unallocated = []

# Allocate classrooms
for course in courses:
    name, students, period = course
    assigned = False

    for room in rooms:
        room_name, capacity = room

        # Check room capacity
        if capacity >= students:
            clash = False

            # Check timetable clashes
            for item in allocated:
                if item[1] == room_name and item[2] == period:
                    clash = True

            if not clash:
                allocated.append(
                    (name, room_name, period)
                )
                assigned = True
                break

    if not assigned:
        unallocated.append(name)

# Display timetable
print("--- Classroom Timetable ---")

for item in allocated:
    print(item[0], "-", item[1], "-", item[2])

# Display unallocated courses
print("\nUnallocated Courses:", unallocated)

if len(unallocated) == 0:
    print("All courses are accommodated.")
else:
    print("All courses cannot be accommodated.")

print("\nTotal Courses:", len(courses))
print("Allocated Courses:", len(allocated))
print("Unallocated Courses:", len(unallocated))
