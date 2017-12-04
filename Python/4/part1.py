valid_inputs = 0

with open("input", "r") as the_input:
    for line in the_input:
        words = line.split()
        if len(words) == len(set(words)):
            valid_inputs += 1

print(valid_inputs)



