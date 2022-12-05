import re

with open("05.txt", "r") as f:
    pattern = re.compile(r"[A-Z]")
    stacks = []

    while (a := f.readline())[1] != "1":
        # use regex to find all capital letters in line
        for match in pattern.finditer(a):
            letter = match[0]
            stack_nr = (match.start() - 1) // 4
            while stack_nr >= len(stacks):
                stacks.append([])
            stacks[stack_nr].insert(0, letter)
    
    # skip empty line
    f.readline()

    move_pattern = re.compile(r"move (\d+) from (\d) to (\d)\n")
    while a := f.readline():
        move_nr, from_stack, to_stack = [int(s) for s in move_pattern.match(a).groups()]

        stacks[to_stack - 1] += stacks[from_stack - 1][-move_nr:]
        stacks[from_stack - 1] = stacks[from_stack - 1][:-move_nr]
    
    print("".join(s[-1] for s in stacks))
