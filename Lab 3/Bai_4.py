import math

while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break

S1 = sum(i for i in range(1, n + 1))
S2 = sum(1 / i for i in range(1, n + 1))
S3 = sum(1 / math.sqrt(2 * i) for i in range(1, n + 1))
S4 = sum(((-1)**(i + 1)) / i for i in range(1, n + 1))

print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")
print(f"S4 = {S4}")