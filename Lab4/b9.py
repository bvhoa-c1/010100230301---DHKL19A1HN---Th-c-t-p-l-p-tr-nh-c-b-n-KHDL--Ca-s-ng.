while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    chọn = int(input("Chọn: "))
    if chọn == 0:
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if chọn == 1:
        print("Kq", a+b)
    elif chọn == 2:
        print("Kq", a-b)
    elif chọn == 3:
        print("Kq", a*b)
    elif chọn == 4:
        if b != 0:
            print("kq:", a/b)
        else:
            print("ko chia đc")