program_dict = {}

with open("input", "r") as the_input:
    for line in the_input:
        try:
            program_dict[line.split()[0]] = [program.strip() for program in line.split("->")[1].split(",")]
        except IndexError:
            program_dict[line.split()[0]] = []


for program, disk in program_dict.items():
    if disk != []:
        flag = 0
        for disk_elements in program_dict.values():
            if program in disk_elements and flag == 0:
                flag = 1
        if flag == 0:
            print(program)
