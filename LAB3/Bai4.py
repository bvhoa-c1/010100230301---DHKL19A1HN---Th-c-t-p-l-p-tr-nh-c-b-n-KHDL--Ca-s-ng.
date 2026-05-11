import math

while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại n > 0!")

# a) S1 = 1 + 2 + ... + n
S1 = 0
for i in range(1, n + 1):
    S1 += i
print(f"S1 = {S1}")

# b) S2 = 1/1 + 1/2 + ... + 1/n
S2 = 0
for i in range(1, n + 1):
    S2 += 1 / i
print(f"S2 = {S2}")

# c) S3 = 1/căn(2) + 1/căn(4) + ... + 1/căn(2n)
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)
print(f"S3 = {S3}")

# d) S4 = 1/1 - 1/2 + 1/3 - ... + (-1)^(n+1)/n
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1)**(i + 1)) / i
print(f"S4 = {S4}")