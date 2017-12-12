def check_childrens(node):
    """Check each clild of a node."""
    for child in id_dict[node]:
        if child not in zero_list:
            zero_list.append(child)
            check_childrens(child)


id_dict = {}
group_list = []

with open("input") as the_input:
    for line in the_input:
        id_dict[int(line.split()[0])] = [int(item) for item in line.split(">")[1].split(", ")]

for identificator in id_dict.keys():
    zero_list = []
    check_childrens(identificator)
    zero_list.sort()
    if zero_list not in group_list:
        group_list.append(zero_list)

print(len(group_list))
