import re

SEARCH_AREA_SIZE = 4000000

sensors = []

for line in open("15.txt", "r"):
    sx, sy, bx, by = [int(x) for x in re.findall(r"=(-?\d+)", line)]
    sensors.append((sx, sy, abs(bx - sx) + abs(by - sy)))  # x, y, distance

for y in range(SEARCH_AREA_SIZE + 1):
    print(y)
    covered_ranges = []  # list of disjoint ranges (both ends inclusive)

    def add_range(start, end):
        ranges_to_remove = []

        for i, (s, e) in enumerate(covered_ranges):
            if not (end < s - 1 or start > e + 1):
                start = min(start, s)
                end = max(end, e)
                ranges_to_remove.append(i)
        
        for i in reversed(ranges_to_remove):
            del covered_ranges[i]
        
        covered_ranges.append((start, end))

    for sx, sy, d in sensors:
        w = d - abs(sy - y)

        left = sx - w
        right = sx + w

        if w > 0 and left <= SEARCH_AREA_SIZE and right >= 0:
            add_range(max(0, left), min(right, SEARCH_AREA_SIZE))
    
    if len(covered_ranges) == 2:
        print((covered_ranges[0][1] + 1) * 4000000 + y)
        break
