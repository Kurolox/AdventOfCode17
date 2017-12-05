with open("input", "r") as the_input:
    input_dict = [int(number) for number in the_input]

try:
    steps = 0
    index = 0
    while True:
        input_dict[index] += 1
        index += input_dict[index] - 1
        steps += 1

except IndexError:
    print(steps)
