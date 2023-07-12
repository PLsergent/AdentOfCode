from math import sqrt


with open('./advent9.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

def calculate_distance(head, tail):
    return int(sqrt((tail[0] - head[0]) ** 2 + (tail[1] - head[1]) ** 2))

def where_to_move(head, tail):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            return (tail[0], head[1] - 1)
        elif head[1] < tail[1]:
            return (tail[0], head[1] + 1)
    if head[1] == tail[1]:
        if head[0] > tail[0]:
            return (head[0] - 1, tail[1])
        elif head[0] < tail[0]:
            return (head[0] + 1, tail[1])
    if head[0] - tail[0] == 2:
        if head[1] > tail[1]:
            return (tail[0] + 1, tail[1] + 1)
        else:
            return (tail[0] + 1, tail[1] - 1)
    if head[0] - tail[0] == -2:
        if head[1] > tail[1]:
            return (tail[0] - 1, tail[1] + 1)
        else:
            return (tail[0] - 1, tail[1] - 1)
    if head[1] - tail[1] == 2:
        if head[0] > tail[0]:
            return (tail[0] + 1, tail[1] + 1)
        else:
            return (tail[0] - 1, tail[1] + 1)
    if head[1] - tail[1] == -2:
        if head[0] > tail[0]:
            return (tail[0] + 1, tail[1] - 1)
        else:
            return (tail[0] - 1, tail[1] - 1)
    return tail

# Part 1

# head = (0, 0)
# tail = (0, 0)
# tails_pos = set()
# tails_pos.add(tail)

# for line in content:
    # line_split = line.split(" ")
    # direction = line_split[0]
    # distance = int(line_split[1])

    # if direction == "R":
    #     for pos in range(distance):
    #         head = (head[0] + 1, head[1])
    #         d = calculate_distance(head, tail)
    #         if d > 1:
    #             if head[1] == tail[1]:
    #                 tail = (tail[0] + 1, tail[1])
    #             else:
    #                 tail = (tail[0] + 1, head[1])
    #             tails_pos.add(tail)
    # elif direction == "L":
    #     for pos in range(distance):
    #         head = (head[0] - 1, head[1])
    #         d = calculate_distance(head, tail)
    #         if d > 1:
    #             if head[1] == tail[1]:
    #                 tail = (tail[0] - 1, tail[1])
    #             else:
    #                 tail = (tail[0] - 1, head[1])
    #             tails_pos.add(tail)
    # elif direction == "U":
    #     for pos in range(distance):
    #         head = (head[0], head[1] + 1)
    #         d = calculate_distance(head, tail)
    #         if d > 1:
    #             if head[0] == tail[0]:
    #                 tail = (tail[0], tail[1] + 1)
    #             else:
    #                 tail = (head[0], tail[1] + 1)
    #             tails_pos.add(tail)
    # elif direction == "D":
    #     for pos in range(distance):
    #         head = (head[0], head[1] - 1)
    #         d = calculate_distance(head, tail)
    #         if d > 1:
    #             if head[0] == tail[0]:
    #                 tail = (tail[0], tail[1] - 1)
    #             else:
    #                 tail = (head[0], tail[1] - 1)
    #             tails_pos.add(tail)

points = [(0, 0)] * 2
twos_pos = set()
twos_pos.add((0, 0))

for line in content:
    line_split = line.split(" ")
    direction = line_split[0]
    distance = int(line_split[1])

    if direction == "R":
        for pos in range(distance):
            for i in range(len(points)-1):
                points[i] = (points[i][0] + 1, points[i][1])
                points[i + 1] = where_to_move(points[i], points[i + 1])
                twos_pos.add(points[i + 1])
                
    elif direction == "L":
        for _ in range(distance):
            for i in range(len(points)-1):
                points[i] = (points[i][0] - 1, points[i][1])
                points[i + 1] = where_to_move(points[i], points[i + 1])
                twos_pos.add(points[i + 1])
                    
    elif direction == "U":
        for _ in range(distance):
            for i in range(len(points)-1):
                points[i] = (points[i][0], points[i][1] + 1)
                points[i + 1] = where_to_move(points[i], points[i + 1])
                twos_pos.add(points[i + 1])
                    
    elif direction == "D":
        for _ in range(distance):
            for i in range(len(points)-1):
                points[i] = (points[i][0], points[i][1] - 1)
                points[i + 1] = where_to_move(points[i], points[i + 1])
                twos_pos.add(points[i + 1])

print(len(twos_pos))

# Part 2

points = [(0, 0)] * 10
nines_pos = set()
nines_pos.add((0, 0))

for line in content:
    line_split = line.split(" ")
    direction = line_split[0]
    distance = int(line_split[1])

    if direction == "R":
        for _ in range(distance):
            for i in range(len(points)-1):
                if i == 0:
                    points[i] = (points[i][0] + 1, points[i][1])
                points[i + 1] = where_to_move(points[i], points[i + 1])
                if i == 8:
                    nines_pos.add(points[i + 1])
    elif direction == "L":
        for _ in range(distance):
            for i in range(len(points)-1):
                if i == 0:
                    points[i] = (points[i][0] - 1, points[i][1])
                points[i + 1] = where_to_move(points[i], points[i + 1])
                if i == 8:
                    nines_pos.add(points[i + 1])
    elif direction == "U":
        for _ in range(distance):
            for i in range(len(points)-1):
                if i == 0:
                    points[i] = (points[i][0], points[i][1] + 1)
                points[i + 1] = where_to_move(points[i], points[i + 1])
                if i == 8:
                    nines_pos.add(points[i + 1])
    elif direction == "D":
        for _ in range(distance):
            for i in range(len(points)-1):
                if i == 0:
                    points[i] = (points[i][0], points[i][1] - 1)
                points[i + 1] = where_to_move(points[i], points[i + 1])
                if i == 8:
                    nines_pos.add(points[i + 1])

print(len(nines_pos))