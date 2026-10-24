
# Campus Festival Registration and Financial Audit

participants = ["Cherry", "Bhavana", "Joshika", "Lowkika", "Navya"]
registration_fee = 200

sponsorship = 5000
expenses = 3000

# Count registrations and fees
total_registrations = len(participants)
total_fees = total_registrations * registration_fee

# Find duplicate registrations
duplicates = []

for i in range(len(participants)):
    for j in range(i + 1, len(participants)):
        if participants[i] == participants[j]:
            if participants[i] not in duplicates:
                duplicates.append(participants[i])

# Count unique participants
unique_participants = []

for name in participants:
    if name not in unique_participants:
        unique_participants.append(name)

# Calculate financial balance
total_income = (
    len(unique_participants) * registration_fee
    + sponsorship
)

balance = total_income - expenses

# Display audit report
print("--- Campus Festival Audit ---")
print("Total Registrations:", total_registrations)
print("Unique Participants:", len(unique_participants))
print("Total Registration Fees:", len(unique_participants) * registration_fee)
print("Sponsorship Contributions:", sponsorship)
print("Total Income:", total_income)
print("Total Expenses:", expenses)
print("Final Financial Balance:", balance)

print("Duplicate Registrations:", duplicates)
