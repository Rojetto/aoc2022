length = 10
rope = [(0, 0)] * length

tail_visited_pos = set([rope[-1]])

def cmp(a, b):
    return (a > b) - (a < b) 

for line in open("09.txt", "r"):
    for i in range(int(line[2:-1])):
        match line[0]:
            case "U": rope[0] = (rope[0][0], rope[0][1] + 1)
            case "D": rope[0] = (rope[0][0], rope[0][1] - 1)
            case "L": rope[0] = (rope[0][0] - 1, rope[0][1])
            case "R": rope[0] = (rope[0][0] + 1, rope[0][1])
        
        for i in range(1, length):
            if max(abs(rope[i-1][0] - rope[i][0]), abs(rope[i-1][1] - rope[i][1])) > 1:
                rope[i] = rope[i][0] + cmp(rope[i-1][0], rope[i][0]), rope[i][1] + cmp(rope[i-1][1], rope[i][1])
        
        tail_visited_pos.add(rope[-1])

print(len(tail_visited_pos))
