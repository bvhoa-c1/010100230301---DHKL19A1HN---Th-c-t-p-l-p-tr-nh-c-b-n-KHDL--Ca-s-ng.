# Nhập n > 10
while True:
    n = int(input("Nhập n (>10): "))
    if n > 10:
        break
    print("Nhập lại!")

# a) S1 = 6 + 6^2 + 6^3 + ... (dừng khi > n)
S1 = 0
a = 1
while 6**a <= n:
    S1 += 6**a
    a += 1

# b) S2 = 1/3 + 1/3^2 + 1/3^3 + ...
S2 = 0
a = 1
while 3**a <= n:
    S2 += 1 / (3**a)
    a += 1

# c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
S3 = 0
a = 1
while a**2 <= n:
    S3 += ((-1)**a) * (a**2)
    a += 1

# d) S4 = 1*2*3 + 2*3*4 + ... + a(a+1)(a+2)
S4 = 0
a = 1
while a*(a+1)*(a+2) <= n:
    S4 += a*(a+1)*(a+2)
    a += 1

# In kết quả
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)