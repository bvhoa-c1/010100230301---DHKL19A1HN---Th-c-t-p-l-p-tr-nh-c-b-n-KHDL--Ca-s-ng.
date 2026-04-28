#a
n = int(input("Nhap n: "))
i = 1
S1 = 0
while i <= n:
    S1 += 6 ** i
    i += 1
print("S1 =", S1)

#b
n = int(input("Nhap n: "))
i = 1
S2 = 0
while i <= n:
    S2 += 1 / (3 ** i)
    i += 1
print("S2 =", S2)

#c
n = int(input("Nhap n: "))
i = 1
S3 = 0
while i <= n:
    S3 += ((-1) ** i) * (i ** 2)
    i += 1
print("S3 =", S3)

#d
n = int(input("Nhap n: "))
i = 1
S4 = 0
while i <= n:
    S4 += i * (i + 1) * (i + 2)
    i += 1
print("S4 =", S4)