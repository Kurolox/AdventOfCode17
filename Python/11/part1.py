with open("input") as the_input:
    for line in the_input:
        direction_list = [direction.strip() for direction in line.split(",")]

move_count = {"n": 0, "s": 0, "nw": 0, "ne": 0, "sw": 0, "se": 0}

for direction in direction_list:  # This is so ugly, I wish I knew anything better.
    if direction == "n":
        move_count["n"] += 1
    elif direction == "s":
        move_count["s"] += 1
    elif direction == "nw":
        move_count["nw"] += 1
    elif direction == "ne":
        move_count["ne"] += 1
    elif direction == "sw":
        move_count["sw"] += 1
    elif direction == "se":
        move_count["se"] += 1

axis_1 = abs(move_count["n"] - move_count["s"])
axis_2 = abs(move_count["ne"] - move_count["sw"])
axis_3 = abs(move_count["nw"] - move_count["se"])

print(axis_1 + max(axis_2, axis_3))
