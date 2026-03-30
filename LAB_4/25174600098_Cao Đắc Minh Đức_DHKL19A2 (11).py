n = int(input("Nhập số nguyên n (n > 10): "))

# a) S1 = 6 + 6^2 + 6^3 + ... + 6^n
s1 = 0
a = 1
while a <= n:
    s1 += 6**a
    a += 1
print(f"a) S1 = {s1}")

# b) S2 = 1/3 + 1/3^3 + 1/3^5 + ... + 1/3^(2n+1)
s2 = 0
a = 0
while a <= n:
    s2 += 1 / (3**(2*a + 1))
    a += 1
print(f"b) S2 = {s2}")

# c) S3 = -1^2 + 2^2 - 3^2 + ... + ((-1)^n)*(n^2)
s3 = 0
a = 1
while a <= n:
    s3 += ((-1)**a) * (a**2)
    a += 1
print(f"c) S3 = {s3}")

# d) S4 = 1.2.3 + 2.3.4 + ... + n.(n+1).(n+2)
s4 = 0
a = 1
while a <= n:
    s4 += a * (a + 1) * (a + 2)
    a += 1
print(f"d) S4 = {s4}")