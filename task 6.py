
# Nested List Examination Seating Validation

# Seating matrix (0 means empty seat)
seats = [
    [101, 102, 0],
    [103, 101, 104],
    [105, 999, 106]
]

# Reserved seat positions (row, column)
reserved = [(0, 2)]

# Valid student roll numbers
valid_rolls = [101, 102, 103, 104, 105, 106]

roll_numbers = []
duplicates = []
empty_seats = []
invalid = []
reserved_errors = []

# Check each seat
for i in range(len(seats)):
    for j in range(len(seats[i])):
        roll = seats[i][j]

        if (i, j) in reserved:
            if roll != 0:
                reserved_errors.append((i + 1, j + 1))

        if roll == 0:
            if (i, j) not in reserved:
                empty_seats.append((i + 1, j + 1))

        elif roll not in valid_rolls:
            invalid.append(roll)

        else:
            if roll in roll_numbers:
                if roll not in duplicates:
                    duplicates.append(roll)
            else:
                roll_numbers.append(roll)

# Display results
print("--- Examination Seating Validation ---")
print("Duplicate Roll Numbers:", duplicates)
print("Empty Seats (Row, Column):", empty_seats)
print("Invalid Roll Numbers:", invalid)
print("Reserved Seat Errors:", reserved_errors)

if not duplicates and not empty_seats and not invalid and not reserved_errors:
    print("Seating arrangement is valid.")
else:
    print("Seating arrangement has errors.")
