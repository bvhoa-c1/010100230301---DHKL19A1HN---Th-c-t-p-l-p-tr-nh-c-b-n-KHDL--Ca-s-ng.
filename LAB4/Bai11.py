# Yêu cầu bắt buộc n > 10
n = int(input("Nhập số nguyên n (n > 10): "))
while n <= 10:
    n = int(input("n phải lớn hơn 10. Vui lòng nhập lại: "))

print(f"\nKết quả với n = {n}:")

# a) S1 = 6 + 6^2 + ... + 6^a
S1 = 0
a = 1
while a <= n:
    S1 += 6 ** a
    a += 1
print(f"a) S1 = {S1}")

# b) S2 = 1/3 + 1/3^3 + ... + 1/3^(2a+1)
# Để phần tử đầu tiên là 1/3^1, a phải bắt đầu từ 0
S2 = 0
a = 0
while a <= n:
    S2 += 1 / (3 ** (2 * a + 1))
    a += 1
print(f"b) S2 = {S2}")

# c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
S3 = 0
a = 1
while a <= n:
    S3 += ((-1) ** a) * (a ** 2)
    a += 1
print(f"c) S3 = {S3}")

# d) S4 = 1.2.3 + 2.3.4 + ... + a*(a+1)*(a+2)
S4 = 0
a = 1
while a <= n:
    S4 += a * (a + 1) * (a + 2)
    a += 1
print(f"d) S4 = {S4}")