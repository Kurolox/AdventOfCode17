with open("input", "r") as the_input:
    full_input = "".join([line for line in the_input])

index = 0
garbage_mode = False
value_counter = 0
total_value = 0

while index < len(full_input):
    if garbage_mode:
        if full_input[index] == "!":
            index += 1
        elif full_input[index] == ">":
            garbage_mode = False
    else:
        if full_input[index] == "<":
            garbage_mode = True
        elif full_input[index] == "{":
            value_counter += 1
        elif full_input[index] == "}":
            total_value += value_counter
            value_counter -= 1

    index += 1

print(total_value)
