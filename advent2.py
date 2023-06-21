with open('./advent2.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors
# A beats Z, B beats X, C beats Y
# X: 1, Y: 2, Z: 3
# Win: 6, Draw: 3, Lose: 0

# Part 1

results = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

sum = 0
for i in content:
   sum += results[i]

print(sum)

# Part 2

# X: loose, Y: draw, Z: win

results = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

sum = 0
for i in content:
    sum += results[i]

print(sum)