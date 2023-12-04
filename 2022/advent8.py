with open('./advent8.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# fill rows and cols
rows = [[] for _ in content]
cols = [[] for _ in content[0]]

for i, line in enumerate(content):
    for j, tree in enumerate(line):
        rows[i].append(tree)
        cols[j].append(tree)


# Part 1

visible_trees = 0
for i, row in enumerate(rows):
    # check if on edge
    if i == 0 or i == len(rows) - 1:
        visible_trees += len(row)
        continue
    for j, tree in enumerate(row):
        if j == 0 or j == len(row) - 1:
            visible_trees += 1
            continue
        
        visible = 4
        # check visible from row-left
        for tree_left in row[:j]:
            if int(tree_left) >= int(tree):
                visible -= 1
                break
        
        # check visible from row-right
        for tree_right in row[j+1:]:
            if int(tree_right) >= int(tree):
                visible -= 1
                break
        
        # check visible from col-up
        for tree_up in cols[j][:i]:
            if int(tree_up) >= int(tree):
                visible -= 1
                break
        
        # check visible from col-down
        for tree_down in cols[j][i+1:]:
            if int(tree_down) >= int(tree):
                visible -= 1
                break
        
        if visible > 0:
            visible_trees += 1

print(visible_trees)


# Part 2

scores = []
visible_trees = 0
for i, row in enumerate(rows):
    # check if on edge
    if i == 0 or i == len(rows) - 1:
        visible_trees += len(row)
        continue
    for j, tree in enumerate(row):
        if j == 0 or j == len(row) - 1:
            visible_trees += 1
            continue
        
        # check visible from row-left
        visible_left = 0
        for tree_left in list(reversed(row[:j])):
            if int(tree_left) < int(tree):
                visible_left += 1
            else:
                visible_left += 1
                break
        
        # check visible from row-right
        visible_right = 0
        for tree_right in row[j+1:]:
            if int(tree_right) < int(tree):
                visible_right += 1
            else:
                visible_right += 1
                break
        
        # check visible from col-up
        visible_up = 0
        for tree_up in list(reversed(cols[j][:i])):
            if int(tree_up) < int(tree):
                visible_up += 1
            else:
                visible_up += 1
                break
        
        # check visible from col-down
        visible_down = 0
        for tree_down in cols[j][i+1:]:
            if int(tree_down) < int(tree):
                visible_down += 1
            else:
                visible_down += 1
                break

        score = visible_left * visible_right * visible_up * visible_down
        scores.append(score)

scores.sort()
print(scores[-1])