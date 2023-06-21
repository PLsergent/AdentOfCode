with open('./advent6.txt') as f:
    content = f.readlines()

content = content[0].strip()

# Part 1
for i, char in enumerate(content):
    potential_marker = content[i:i+4]
    set_potential_marker = set(potential_marker)
    if len(set_potential_marker) == 4:
        print(char, i+4)
        break

# Part 2
for i, char in enumerate(content):
    potential_marker = content[i:i+14]
    set_potential_marker = set(potential_marker)
    if len(set_potential_marker) == 14:
        print(char, i+14)
        break
