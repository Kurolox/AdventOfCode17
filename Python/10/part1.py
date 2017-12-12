with open("input") as the_input:
    for line in the_input:
        lenght_list = [int(lenght) for lenght in line.split(",")]


number_list = [num for num in range(256)]

index_position = 0
skip_track = 0

for lenght in lenght_list:
    slice_to_modify = (number_list*2)[index_position:index_position + lenght]
    for i, number in enumerate(slice_to_modify):
        number_list[(index_position+lenght-i-1)%len(number_list)] = number

    index_position = (index_position + lenght + skip_track) % len(number_list)
    skip_track += 1

print(number_list[0] *  number_list[1])
