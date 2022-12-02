with open("01.txt", "r") as f:
    highest = 0
    acc = 0

    while a := f.readline():
        if a.strip():
            acc += int(a.strip())
            highest = max(highest, acc)
        else:
            acc = 0
    
    print(highest)
