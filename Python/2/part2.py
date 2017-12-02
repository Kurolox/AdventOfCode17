checksum = 0


with open("the_input", "r") as the_input:
    for line in the_input:
        numlist = [int(num) for num in line.split()]
        for number1 in numlist:
            for number2 in numlist:
                if number1 % number2 == 0 and number1 != number2:
                    checksum += number1 // number2

        
print(checksum)
