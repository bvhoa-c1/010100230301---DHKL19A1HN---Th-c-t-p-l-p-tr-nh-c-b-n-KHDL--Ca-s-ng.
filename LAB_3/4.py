from math import *
n = int(input())
if n <= 0:
    exit()
tong = 0
tong_2 = 0
tong_3 = 0
tong_4 = 0

for i in range(1, n + 1):
    tong += i
    tong_2 += 1 / i
    tong_3 += 1 / (sqrt(2 * i))
    tong_4 += ((-1)**(i + 1)) / i
print(tong)
print(tong_2)
print(tong_3)
print(tong_4)