n = int(input("Nhập vào số nguyên dương: "))
if n == 0:
    print("kết quả nhị phân: 0")
else:
    kq = " "
    temp = n
    while temp > 0:
        so_du = temp %2
        kq = str(so_du) +  kq
        temp = temp // 2
    print("Số", n, "Số nhị phân là:", kq)