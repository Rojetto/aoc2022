with open("01.txt", "r") as f:
    sums = []
    acc = 0

    while a := f.readline():
        if a.strip():
            acc += int(a.strip())
        else:
            sums.append(acc)
            acc = 0
    else:
        sums.append(acc)

    print(sum(sorted(sums, reverse=True)[0:3]))
    
