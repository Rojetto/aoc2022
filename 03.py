with open("03.txt", "r") as f:
    acc = 0
    while line := f.readline().strip():
        comp1 = line[:len(line) // 2]
        comp2 = line[len(line) // 2:]

        for item in comp1:
            if item in comp2:
                if 'a' <= item <= 'z':
                    acc += ord(item) - ord('a') + 1
                else:
                    acc += ord(item) - ord('A') + 27

                break

    print(acc)
