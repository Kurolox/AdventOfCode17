import math

target = int(input())
size = math.ceil(math.sqrt(target))  # Since it's a cube, we can take the square of the input and round up to the nearest odd number to find the biggest square that contains the number.

dist_1 = (size-1) / 2

dist_2 = math.pow(size, 2) - target

total_dist = dist_1 + (dist_1-int(dist_2))
print(abs(int(total_dist)))
