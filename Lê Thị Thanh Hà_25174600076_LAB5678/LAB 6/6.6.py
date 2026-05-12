n = int(input("Nhập số lượng phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

if n < 2:
    print("Không đủ phần tử")
else:
    d = a[1] - a[0]
    check = True

    for i in range(2, n):
        if a[i] - a[i-1] != d:
            check = False
            break

    if check:
        print("Là cấp số cộng")
    else:
        print("Không phải cấp số cộng")
