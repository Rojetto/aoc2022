combos = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

with open("02.txt", "r") as f:
    total_score = 0

    while a := f.readline():
        total_score += combos[a.rstrip()]

    print(total_score)
