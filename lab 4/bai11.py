
n = int(input("Nhập số nguyên n (n > 10): "))
#a
S1 = 0
i = 1
while i <= n:
    S1 += 6 ** i
    i += 1
print("S1 =", S1)
#b
S2 = 0
i = 1   # số mũ bắt đầu từ 1
dem = 1 # đếm số hạng
while dem <= n:
    S2 += 1 / (3 ** i)
    i += 2
    dem += 1
print("S2 =", S2)
#c
S3 = 0
i = 1
while i <= n:
    if i % 2 == 1:
        S3 -= i ** 2
    else:
        S3 += i ** 2
    i += 1
print("S3 =", S3)
#d
S4 = 0
i = 1
while i <= n:
    S4 += i * (i + 1) * (i + 2)
    i += 1
print("S4 =", S4)