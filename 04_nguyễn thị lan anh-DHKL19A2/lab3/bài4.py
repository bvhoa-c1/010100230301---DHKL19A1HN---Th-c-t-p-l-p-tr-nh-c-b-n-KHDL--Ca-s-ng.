n = int(input("Nhập n (>0): "))
while n <= 0:
    n = int(input("Nhập lại n (>0): "))

# a
S1 = 0
for i in range(1, n+1):
    S1 += i

# b
S2 = 0
for i in range(1, n+1):
    S2 += 1/i

# c
import math
S3 = 0
for i in range(1, n+1):
    S3 += 1 / math.sqrt(2*i)

# d
S4 = 0
for i in range(1, n+1):
    S4 += ((-1)**(i+1)) / i

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)