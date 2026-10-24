
# Hackathon Team Formation and Ranking

teams = [
    ["Team A", ["Cherry", "Bhavana"], [90, 90]],
    ["Team B", ["Lucky", "Gowri", "Hansitha"], [85, 85]],
    ["Team C", ["Joshika", "Purandeswari"], [80, 90]]
]

min_size = 2
max_size = 3

results = []

for team in teams:
    name = team[0]
    members = team[1]
    scores = team[2]

    # Validate team size
    if len(members) < min_size or len(members) > max_size:
        print(name, "- Invalid team size")
        continue

    # Calculate total and average score
    total = sum(scores)
    average = total / len(scores)

    results.append([name, members, total, average])

# Rank by total score, then average score
results.sort(key=lambda x: (x[2], x[3]), reverse=True)

# Display rankings
print("\n--- Hackathon Team Rankings ---")

rank = 1

for team in results:
    print("\nRank:", rank)
    print("Team:", team[0])
    print("Members:", team[1])
    print("Total Score:", team[2])
    print("Average Score:", round(team[3], 2))
    rank += 1
