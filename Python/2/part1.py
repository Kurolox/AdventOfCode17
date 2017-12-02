checksum = 0


with open("the_input", "r") as the_input:
    for line in the_input:
        numlist = [int(num) for num in line.split()]
        numlist.sort()
        try:
            checksum += numlist[-1] - numlist[0]
        except IndexError:
            pass
        
print(checksum)
