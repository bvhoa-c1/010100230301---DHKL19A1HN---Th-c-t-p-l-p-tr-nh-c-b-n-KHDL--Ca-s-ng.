n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)
print("Các số nguyên tố hoặc số hoàn hảo là:")
for x in a:
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        if x >= 2:
            print(x)

    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        print(x)