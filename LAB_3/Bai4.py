import math
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
    else:
        print("Nhập lại!")
S1 = 0
S2 = 0
S3 = 0
S4 = 0
for i in range(1, n + 1):
    S1 += i
    S2 += 1 / i
    S3 += 1 / math.sqrt(2 * i)
    S4 += ((-1) ** (i + 1)) / i
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)