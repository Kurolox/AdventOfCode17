with open("input") as the_input:
    for line in the_input:
        lenght_list = [ord(char) for char in line]
lenght_list.pop()  # Deleting newline character at end of string
lenght_list += [17, 31, 73, 47, 23]

number_list = [num for num in range(256)]
hash_list = []
index_position = 0
skip_track = 0

for _ in range(64):
    for lenght in lenght_list:
        slice_to_modify = (number_list*2)[index_position:index_position + lenght]
        for i, number in enumerate(slice_to_modify):
            number_list[(index_position+lenght-i-1) % len(number_list)] = number

        index_position = (index_position + lenght + skip_track) % len(number_list)
        skip_track += 1

for i in range(16):
    current_hash = 0
    for number in number_list[16*i:16*(i+1)]:
        current_hash ^= number
    hash_list.append(current_hash)

print("".join([format(number, "02x") for number in hash_list]))
