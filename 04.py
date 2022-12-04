import re

# Regex pattern for (number)-(number),(number)-(number)
pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

with open("04.txt", "r") as f:
    count = 0

    while a := f.readline().strip():
        e1min, e1max, e2min, e2max = pattern.match(a).groups()

        # Test whether one range is completely contained in the other
        if (int(e1min) <= int(e2min) <= int(e2max) <= int(e1max) or
            int(e2min) <= int(e1min) <= int(e1max) <= int(e2max)):
            count += 1

    print(count)
