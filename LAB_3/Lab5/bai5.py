import math
for i in range(1, 1001):
    if int(math.sqrt(i)) ** 2 == i:
        print(i, end=" ")