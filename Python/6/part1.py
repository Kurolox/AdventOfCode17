with open("input", "r") as the_input:
    for line in the_input:
        last_state = [int(node) for node in line.split()]

state_list = [last_state[:]]  # Cloning the list
steps = 0

while True:
    steps += 1
    biggest_node = last_state.index(max(last_state))
    blocks_to_redistribute = last_state[biggest_node]
    index = biggest_node
    last_state[biggest_node] = 0
    while blocks_to_redistribute > 0:
        try:
            index += 1
            last_state[index] += 1
        except IndexError:
            index = 0
            last_state[index] += 1
        blocks_to_redistribute -= 1

    if last_state in state_list:
        break

    state_list.append(last_state[:])


print(steps)
