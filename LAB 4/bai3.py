n = int(input("Nhập n: "))

if n <= 1:
    print("Không có ước số thỏa mãn")
else:
    i = n - 1
    while i > 0:
        if n % i == 0:
            print("Ước số lớn nhất (khác n) là:", i)
            break
        i -= 1
