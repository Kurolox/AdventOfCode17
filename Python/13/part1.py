def get_layer_firewall_pos(layer):
    """Gets the position of the firewall scanner in any given layer."""
    index = 0
    reverse = False
    for i in range(layer):
        if index == firewall_dict[layer] - 1:
            reverse = True
        if index == 0:
            reverse = False

        if reverse:
            index -= 1
        else:
            index += 1
    return index
    


with open("input") as the_input:
    firewall_dict = {}
    for line in the_input:
        firewall_dict[int(line.split(": ")[0])] = int(line.split(": ")[1].rstrip())

severity = 0

for layer in range(max(firewall_dict.keys()) + 1):
    if layer in firewall_dict.keys():
        if get_layer_firewall_pos(layer) == 0:
            severity += layer * firewall_dict[layer]
print(severity)
