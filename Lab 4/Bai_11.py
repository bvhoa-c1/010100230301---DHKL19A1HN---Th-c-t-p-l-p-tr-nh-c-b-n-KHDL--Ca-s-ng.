while True:
    n = int(input("Nhập n: "))
    if n > 10:
        break

S1 = 0
S2 = 0
S3 = 0
S4 = 0

a = 1
while a <= n:
    S1 += 6 ** a
    S2 += 1 / (3 ** (2 * a - 1))
    S3 += ((-1) ** a) * (a ** 2)
    S4 += a * (a + 1) * (a + 2)
    a += 1

print(S1)
print(S2)
print(S3)
print(S4)