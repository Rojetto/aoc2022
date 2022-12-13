from functools import cmp_to_key

packets = [[[2]], [[6]]]  # pre-fill with divider packets

f = open("13.txt", "r")

while line := f.readline():
    if line != "\n":
        packets.append(eval(line))


# returns -1 if left < right, 0 if left == right, 1 if left > right
def cmp(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)
    elif isinstance(left, list) and isinstance(right, list):
        for i, j in zip(left, right):
            if cmp(i, j) != 0:
                return cmp(i, j)
        else:
            return cmp(len(left), len(right))
    else:  # one is an int, the other a list
        if isinstance(left, int):
            return cmp([left], right)
        elif isinstance(right, int):
            return cmp(left, [right])

packets.sort(key=cmp_to_key(cmp))

for i, packet in enumerate(packets):
    if packet == [[2]]:
        div1_index = i + 1
    elif packet == [[6]]:
        div2_index = i + 1
        break

print(div1_index * div2_index)
