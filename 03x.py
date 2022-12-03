with open("03.txt", "r") as f:
    acc = 0

    while common_items := set(f.readline().strip()):
        for _ in range(2):
            common_items &= set(f.readline().strip())

        item = common_items.pop()

        if 'a' <= item <= 'z':
            acc += ord(item) - ord('a') + 1
        else:
            acc += ord(item) - ord('A') + 27

    print(acc)
