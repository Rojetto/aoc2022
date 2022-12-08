trees = []

with open('08.txt', "r") as f:
    while line := f.readline():
        trees.append([int(h) for h in line[:-1]])

dim = len(trees)

best_scenic_score = 0

for r in range(dim):
    for c in range(dim):
        tree_height = trees[r][c]

        # check visible trees to the left
        left_visible = 0
        for i in range(c - 1, -1, -1):
            left_visible += 1
            if trees[r][i] >= tree_height:
                break

        # check visible trees to the right
        right_visible = 0
        for i in range(c + 1, dim):
            right_visible += 1
            if trees[r][i] >= tree_height:
                break
        
        # check visible trees to the top
        top_visible = 0
        for i in range(r - 1, -1, -1):
            top_visible += 1
            if trees[i][c] >= tree_height:
                break
        
        # check visible trees to the bottom
        bottom_visible = 0
        for i in range(r + 1, dim):
            bottom_visible += 1
            if trees[i][c] >= tree_height:
                break

        scenic_score = left_visible * right_visible * top_visible * bottom_visible

        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

print(best_scenic_score)
