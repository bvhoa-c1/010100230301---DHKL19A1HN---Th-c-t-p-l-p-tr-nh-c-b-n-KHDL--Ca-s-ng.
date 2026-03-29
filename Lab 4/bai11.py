n = int(input("Nhập số nguyên n (n > 10): "))
while n <= 10:
    n = int(input("n phải > 10, vui lòng nhập lại: "))

# a) 
S1 = 0
a = 1
while a <= n:
    S1 += 6 ** a
    a += 1
print("S1 =", S1)

# b) 
S2 = 0
a = 0
while a <= n:
    S2 += 1 / (3 ** (2 * a + 1))
    a += 1
print("S2 =", S2)

# c) 
S3 = 0
a = 1
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1
print("S3 =", S3)

# d) 
S4 = 0
a = 1
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1
print("S4 =", S4)