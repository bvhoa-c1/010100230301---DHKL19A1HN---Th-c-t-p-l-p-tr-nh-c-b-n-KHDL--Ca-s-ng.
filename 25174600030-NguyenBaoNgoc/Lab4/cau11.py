n = int(input("Nhập n (n > 10): "))

# a) S1 = 6 + 6^2 + 6^3 + ... + 6^a (a ≤ n)
S1 = 0
i = 1
while i <= n:
    S1 += 6 ** i
    i += 1

print("S1 =", S1)


# b) S2 = 1/3 + 1/3^3 + 1/3^5 + ... (số mũ lẻ ≤ n)
S2 = 0
i = 1
while i <= n:
    S2 += 1 / (3 ** i)
    i += 2

print("S2 =", S2)


# c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
S3 = 0
i = 1
while i <= n:
    S3 += ((-1) ** i) * (i ** 2)
    i += 1

print("S3 =", S3)


# d) S4 = 1*2*3 + 2*3*4 + ... + a*(a+1)*(a+2)
S4 = 0
i = 1
while i <= n:
    S4 += i * (i + 1) * (i + 2)
    i += 1

print("S4 =", S4)