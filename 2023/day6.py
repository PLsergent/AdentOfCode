with open('./day6.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

times = content[0].split(": ")[1].split(" ")
distances = content[1].split(": ")[1].split(" ")

times_striped = [x for x in times if x != ""]
distances_striped = [x for x in distances if x != ""]

total = 0
total_mul = []
for time, record in zip(times_striped, distances_striped):
    speed = 0
    for hold in range(1, int(time)):
        left = int(time) - hold
        speed += 1
        if left * speed > int(record):
            total += 1
    total_mul.append(total)
    total = 0

mul = 1
for total in total_mul:
    mul *= total
print(mul)

# Part 2

times = content[0].split(": ")[1].split(" ")
distances = content[1].split(": ")[1].split(" ")

times_striped = [x for x in times if x != ""]
distances_striped = [x for x in distances if x != ""]

time_strip = "".join(times_striped)
distances_strip = "".join(distances_striped)

total = 0
speed = 0
for hold in range(1, int(time_strip)):
    left = int(time_strip) - hold
    speed += 1
    if left * speed > int(distances_strip):
        total += 1

print(total)