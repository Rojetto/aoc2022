signal = open("06.txt", "r").read()

last_four_chars = []

for i, c in enumerate(signal):
    last_four_chars.append(c)

    if i >= 4:
        del last_four_chars[0]

    if i < 3:
        continue

    found_dupes = False

    for i1 in range(4):
        for i2 in range(3):
            if i1 != i2 and last_four_chars[i1] == last_four_chars[i2]:
                found_dupes = True

    if not found_dupes:
        print(i + 1)
        break
