id_dict = {}
zero_list = []

with open("input") as the_input:
    for line in the_input:
        id_dict[int(line.split()[0])] = [int(item) for item in line.split(">")[1].split(", ")]


def check_childrens(node):
    """Check each clild of a node."""
    for child in id_dict[node]:
        if child not in zero_list:
            zero_list.append(child)
            check_childrens(child)


check_childrens(0)
print(len(zero_list))    
