
# University Admission Decision Engine

applicants = [
    ["cherry", 85, 78, 90],
    ["bhavana", 92, 88, 95],
    ["navya", 70, 65, 60],
    ["lucky", 88, 90, 85]
]

eligible = []

# Admission requirements
minimum_subject_mark = 40
minimum_aggregate = 70
minimum_math_mark = 60

# Check each applicant
for student in applicants:
    name = student[0]
    math = student[1]
    physics = student[2]
    chemistry = student[3]

    aggregate = (math + physics + chemistry) / 3

    if (math >= minimum_subject_mark
            and physics >= minimum_subject_mark
            and chemistry >= minimum_subject_mark
            and math >= minimum_math_mark
            and aggregate >= minimum_aggregate):

        eligible.append([name, aggregate, math])

# Rank by aggregate, then Mathematics marks
eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Display ranked eligible applicants
print("--- University Admission Results ---")

if len(eligible) == 0:
    print("No eligible applicants.")
else:
    rank = 1

    for student in eligible:
        print("\nRank:", rank)
        print("Name:", student[0])
        print("Aggregate:", round(student[1], 2))
        print("Mathematics Marks:", student[2])
        rank += 1

print("\nTotal Applicants:", len(applicants))
print("Eligible Applicants:", len(eligible))
print("Not Eligible Applicants:", len(applicants) - len(eligible))
