pairs = []

f = open("13.txt", "r")

while line1 := f.readline():
    line2 = f.readline()
    f.readline() # blank line

    pairs.append((eval(line1), eval(line2)))


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

right_order_indices = [i + 1 for i, pair in enumerate(pairs) if cmp(pair[0], pair[1]) == -1]
print(sum(right_order_indices))
