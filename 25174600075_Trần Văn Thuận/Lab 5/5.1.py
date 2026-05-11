n = int(input("Nhập vào một số ngyên dương: "))
if n == 0:
    print("kq nhị phân: 0")
else:
    kq = " "
    temp = n
    while temp > 0:
        so_du = temp %2
        kq = str(so_du) +  kq
        temp = temp // 2
    print("Số", n, "Chuyển sang số nhị phân là:", kq)