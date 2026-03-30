import math

n = int(input("Nhập n > 0: "))
while n <= 0:
    n = int(input("Nhập lại n > 0: "))

# a
S1 = sum(range(1, n + 1))

# b
S2 = sum(1/i for i in range(1, n + 1))

# c
S3 = sum(1/math.sqrt(2*i) for i in range(1, n + 1))

# d
S4 = sum(((-1)**(i+1))/i for i in range(1, n + 1))

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)