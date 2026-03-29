import math

# nhập n > 0
while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    print("Nhập lại!")

# a) S1
S1 = 0
for i in range(1, n + 1):
    S1 += i

# b) S2
S2 = 0
for i in range(1, n + 1):
    S2 += 1 / i

# c) S3
S3 = 0
for i in range(1, n + 1):
    S3 += 1 / math.sqrt(2 * i)

# d) S4
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1) ** (i + 1)) / i

# in kết quả
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)