n = int(input("Nhập n (n > 10): "))

while n <= 10:
    n = int(input("Nhập lại n (n > 10): "))

#cau a
S1 = 0
a = 1
while a <= n:
    S1 += 6 ** a
    a += 1

#cau b
S2 = 0
a = 1
while a <= n:
    S2 += 1 / (3 ** (2*a - 1))
    a += 1

#cau c
S3 = 0
a = 1
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1

#cau d
S4 = 0
a = 1
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)