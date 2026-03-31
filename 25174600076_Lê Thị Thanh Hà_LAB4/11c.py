
S3 = 0
i = 1
n=int(input("nhập n:"))
while True:
    term = ((-1) ** i) * (i ** 2)
    if abs(term) > n:
        break
    S3 += term
    i += 1

print("S3 =", S3)
