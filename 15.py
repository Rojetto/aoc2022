import re

CHECK_Y = 2000000

sensors = []
beacons = set()

for line in open("15.txt", "r"):
    sx, sy, bx, by = [int(x) for x in re.findall(r"=(-?\d+)", line)]
    sensors.append((sx, sy, abs(bx - sx) + abs(by - sy)))  # x, y, distance
    beacons.add((bx, by))

covered_ranges = []  # list of disjoint ranges (both ends inclusive)

def add_range(start, end):
    ranges_to_remove = []

    for i, (s, e) in enumerate(covered_ranges):
        if s <= start <= e + 1 or s - 1 <= end <= e:
            start = min(start, s)
            end = max(end, e)
            ranges_to_remove.append(i)
    
    for i in reversed(ranges_to_remove):
        del covered_ranges[i]
    
    covered_ranges.append((start, end))

for sx, sy, d in sensors:
    # get sensor range width at y = CHECK_Y
    w = d - abs(sy - CHECK_Y)

    if w > 0:
        add_range(sx - w, sx + w)

# get the number of beacons inside covered ranges
beacons_in_covered_ranges = [b for b in beacons if any(s <= b[0] <= e for s, e in covered_ranges) and b[1] == CHECK_Y]
spots_covered = sum(e - s + 1 for s, e in covered_ranges)

print(spots_covered - len(beacons_in_covered_ranges))
