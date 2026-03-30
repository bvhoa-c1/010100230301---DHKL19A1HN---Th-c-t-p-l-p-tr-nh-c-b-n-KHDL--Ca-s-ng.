while True:
    print("\n1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Thoat")

    chon = int(input("Chon: "))

    if chon == 0:
        break

    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))

    if chon == 1:
        print("Tong =", a + b)

    elif chon == 2:
        print("Hieu =", a - b)

    elif chon == 3:
        print("Tich =", a * b)

    elif chon == 4:
        if b == 0:
            print("Khong chia duoc")
        else:
            print("Thuong =", a / b)