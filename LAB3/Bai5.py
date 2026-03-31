import math

print("Các số chính phương từ 1 đến 1000 là:")
for i in range(1, 1001):
    can = int(math.sqrt(i))
    if can * can == i:
        print(i, end=" ")
print()