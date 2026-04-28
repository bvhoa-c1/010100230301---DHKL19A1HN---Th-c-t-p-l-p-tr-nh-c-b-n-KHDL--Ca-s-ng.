import math

while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
    print("n phải > 0, nhập lại!")

# a) S1 = 1 + 2 + ... + n
S1 = 0
for i in range(1, n+1):
    S1 += i

# b) S2 = 1 + 1/2 + ... + 1/n
S2 = 0
for i in range(1, n+1):
    S2 += 1/i

# c) S3 = 1/sqrt(2) + 1/sqrt(4) + ... + 1/sqrt(2n)
S3 = 0
for i in range(1, n+1):
    S3 += 1 / math.sqrt(2*i)

# d) S4 = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n
S4 = 0
for i in range(1, n+1):
    S4 += ((-1)**(i+1)) / i

# In kết quả
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)