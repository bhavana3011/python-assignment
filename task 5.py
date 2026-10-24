
# Nested List Sports Performance Analysis

players = [
    ["Cherry", [50, 60, 70]],
    ["Bhavana", [80, 75, 90]],
    ["Lucky", [60, 60, 60]],
    ["Thanu", [70, 85, 80]]
]

results = []

# Analyse each player's performance
for player in players:
    name = player[0]
    scores = player[1]

    total = sum(scores)
    average = total / len(scores)
    consistency = max(scores) - min(scores)

    # Find performance trend
    if scores[-1] > scores[0]:
        trend = "Improving"
    elif scores[-1] < scores[0]:
        trend = "Declining"
    else:
        trend = "Stable"

    results.append(
        [name, total, average, consistency, trend]
    )

# Rank players by total score
# If totals are equal, higher average wins
results.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Display report
print("--- Sports Performance Report ---")

rank = 1

for player in results:
    print("\nRank:", rank)
    print("Player:", player[0])
    print("Total Score:", player[1])
    print("Average Score:", round(player[2], 2))
    print("Score Range:", player[3])
    print("Performance Trend:", player[4])
    rank += 1
