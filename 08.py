trees = []

with open('08.txt', "r") as f:
    while line := f.readline():
        trees.append([int(h) for h in line[:-1]])

dim = len(trees)

total_visible = 0

for r in range(dim):
    for c in range(dim):
        is_visible = False
        tree_height = trees[r][c]

        for i in range(c): # check visibility from the left
            if trees[r][i] >= tree_height:
                break
        else:
            is_visible = True

        for i in range(c+1, dim): # check visibility from the right
            if trees[r][i] >= tree_height:
                break
        else:
            is_visible = True

        for i in range(r): # check visibility from the top
            if trees[i][c] >= tree_height:
                break
        else:
            is_visible = True

        for i in range(r+1, dim): # check visibility from the bottom
            if trees[i][c] >= tree_height:
                break
        else:
            is_visible = True
        
        if is_visible:
            total_visible += 1

print(total_visible)
