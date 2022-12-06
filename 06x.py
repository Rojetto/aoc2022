signal = open("06.txt", "r").read()

last_fourteen_chars = []

for i, c in enumerate(signal):
    last_fourteen_chars.append(c)

    if i >= 14:
        del last_fourteen_chars[0]

    if i < 13:
        continue

    found_dupes = False

    for i1 in range(13):
        for i2 in range(i1+1, 14):
            if i1 != i2 and last_fourteen_chars[i1] == last_fourteen_chars[i2]:
                found_dupes = True

    if not found_dupes:
        print(i + 1)
        break
