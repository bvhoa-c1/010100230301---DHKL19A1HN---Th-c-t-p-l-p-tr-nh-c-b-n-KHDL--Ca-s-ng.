import math

danh_sach_nguyen_to = [
    so for so in range(2, 100)
    if all(so % i != 0 for i in range(2, int(math.sqrt(so)) + 1))
]

print(danh_sach_nguyen_to)