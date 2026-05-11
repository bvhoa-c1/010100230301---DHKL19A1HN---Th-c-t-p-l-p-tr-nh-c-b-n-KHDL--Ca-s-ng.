# Bai 6.6

n = int(input("Nhap so luong phan tu: "))

arr = [int(input()) for _ in range(n)]

if n < 2:
    print("Day co it hon 2 phan tu")
else:
    diff = arr[1] - arr[0]

    is_arithmetic = True

    for i in range(2, n):
        if arr[i] - arr[i - 1] != diff:
            is_arithmetic = False
            break

    if is_arithmetic:
        print("Day la cap so cong")
    else:
        print("Day khong phai cap so cong")