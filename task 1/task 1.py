
# University Hostel Room Allocation

rooms = {
    "Room 101": 2,
    "Room 102": 3,
    "Room 103": 2
}

students = [
    ["cherry", "Male"],
    ["bhavana", "Female"],
    ["joshika", "Female"],
    ["ravi", "Male"],
    ["lucky", "Female"],
    ["thanu", "Female"],
    ["navya", "Female"],
    ["Rahul", "Male"]
]

allocated = []
unallocated = []

# Allocate rooms to students
for student in students:
    name = student[0]
    gender = student[1]
    assigned = False

    for room in rooms:
        if rooms[room] > 0:
            # Keep students grouped by gender
            same_gender = True

            for allocation in allocated:
                if allocation[0] == room:
                    if allocation[2] != gender:
                        same_gender = False

            if same_gender:
                allocated.append([room, name, gender])
                rooms[room] -= 1
                assigned = True
                break

    if not assigned:
        unallocated.append(name)

# Display allocation details
print("--- Hostel Room Allocation ---")

for allocation in allocated:
    print(allocation[1], "->", allocation[0])

print("\nUnallocated Students:", unallocated)
print("Total Unallocated Demand:", len(unallocated))

# Check duplicate assignments
print("\n--- Duplicate Assignment Check ---")
duplicate_found = False

for i in range(len(allocated)):
    for j in range(i + 1, len(allocated)):
        if allocated[i][1] == allocated[j][1]:
            print("Duplicate:", allocated[i][1])
            duplicate_found = True

if not duplicate_found:
    print("No duplicate assignments found.")
