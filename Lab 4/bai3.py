n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

for i in range(n - 1, 0, -1):
    if n % i == 0:
        print("Ước số lớn nhất của", n, "(khác n) là:", i)
        break