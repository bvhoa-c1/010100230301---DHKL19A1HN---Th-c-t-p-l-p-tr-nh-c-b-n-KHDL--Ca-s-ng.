import math

for i in range(1, 1001):
    can = int(math.sqrt(i))   
    if can * can == i:        
        print(i, end=" ")