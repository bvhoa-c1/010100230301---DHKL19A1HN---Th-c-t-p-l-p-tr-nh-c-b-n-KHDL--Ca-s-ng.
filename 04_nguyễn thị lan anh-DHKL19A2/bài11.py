n = int(input("Nhap n (>10): "))

# -------- S1 --------
s1 = 0
i = 1

while i <= n:
    s1 += 6 ** i
    i += 1

# -------- S2 --------
s2 = 0
i = 1

while i <= n:
    s2 += 1 / (3 ** i)
    i += 1

# -------- S3 --------
s3 = 0
i = 1

while i <= n:
    s3 += (-1) ** i * (i ** 2)
    i += 1

# -------- S4 --------
s4 = 0
i = 1

while i <= n:
    s4 += i * (i + 1) * (i + 2)
    i += 1

print("S1 =", s1)
print("S2 =", s2)
print("S3 =", s3)
print("S4 =", s4)