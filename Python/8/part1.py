def modify_values(line):
    """Modifies the dict. It assumes that the condition was met and checked beforehand."""
    if line.split()[1] == "inc":
        register_dict[line.split()[0]] += int(line.split()[2])
    else:
        register_dict[line.split()[0]] -= int(line.split()[2])


register_dict = {}

with open("input", "r") as the_input:
    for line in the_input:
        register_dict[line.split()[0]] = 0

with open("input", "r") as the_input:
    for line in the_input:
        if line.split()[5] == "==":
            if register_dict[line.split()[4]] == int(line.split()[6]):
                    modify_values(line)
        elif line.split()[5] == "!=":
            if register_dict[line.split()[4]] != int(line.split()[6]):
                    modify_values(line)
        elif line.split()[5] == ">=":
            if register_dict[line.split()[4]] >= int(line.split()[6]):
                    modify_values(line)
        elif line.split()[5] == "<=":
            if register_dict[line.split()[4]] <= int(line.split()[6]):
                    modify_values(line)
        elif line.split()[5] == "<":
            if register_dict[line.split()[4]] < int(line.split()[6]):
                    modify_values(line)
        elif line.split()[5] == ">":
            if register_dict[line.split()[4]] > int(line.split()[6]):
                    modify_values(line)


print(max([value for value in register_dict.values()]))
