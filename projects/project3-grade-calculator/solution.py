# Project 3 — Grade Calculator
# Author: Samuel Aguado

scores = []

print("Enter student scores (type -1 to finish):")

while True:
    try:
        score = float(input("Score: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if score == -1:
        break

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        continue

    scores.append(score)

if not scores:
    print("No scores entered.")
else:
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("\n=== Results ===")
    print(f"Number of students: {len(scores)}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")

    print("\nGrade distribution:")

    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for score in scores:
        if score >= 90:
            grades["A"] += 1
        elif score >= 80:
            grades["B"] += 1
        elif score >= 70:
            grades["C"] += 1
        elif score >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1

    for grade, count in grades.items():
        print(f"{grade}: {count}")