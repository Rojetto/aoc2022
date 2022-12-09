head = (0, 0)
tail = (0, 0)

visited_pos = set([(tail)])

def cmp(a, b):
    return (a > b) - (a < b) 

for line in open("09.txt", "r"):
    for i in range(int(line[2:-1])):
        match line[0]:
            case "U": head = (head[0], head[1] + 1)
            case "D": head = (head[0], head[1] - 1)
            case "L": head = (head[0] - 1, head[1])
            case "R": head = (head[0] + 1, head[1])
        
        if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
            tail = tail[0] + cmp(head[0], tail[0]), tail[1] + cmp(head[1], tail[1])
        
        visited_pos.add(tail)

print(len(visited_pos))
