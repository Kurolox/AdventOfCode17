disk_dict = {}
weight_dict = {}
problematic_nodes = []

def find_weight(program):
    #  Check if the program has a disk above itself
    if len(disk_dict[program]) > 0:
        weight = []
        #  If it does, check the weight of each one of said programs
        for i, disk_program in enumerate(disk_dict[program]):
            weight.append(find_weight(disk_program))
        if len(set(weight)) != 1:
            problematic_nodes.append(program)
        return sum(weight) + weight_dict[program]
    return weight_dict[program]


with open("input", "r") as the_input:
    for line in the_input:
        try:
            disk_dict[line.split()[0]] = [program.strip() for program in line.split("->")[1].split(",")]
        except IndexError:
            disk_dict[line.split()[0]] = []
        weight_dict[line.split()[0]] = int(line.split()[1].lstrip("(").rstrip(")"))

for program, weight in disk_dict.items():
    find_weight(program)

#  Now we have a list with nodes causing issues. The one with a weight issue will be the one with the lightest weight, since it will be near the top."
