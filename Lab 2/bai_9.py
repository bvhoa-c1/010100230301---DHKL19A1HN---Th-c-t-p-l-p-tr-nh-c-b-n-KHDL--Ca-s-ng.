while True:
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Thoat")

    choice = int(input("Chon: "))

    if choice == 0:
        break

    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))

    if choice == 1:
        print("Ket qua =", a + b)
    elif choice == 2:
        print("Ket qua =", a - b)
    elif choice == 3:
        print("Ket qua =", a * b)
    elif choice == 4:
        if b != 0:
            print("Ket qua =", a / b)
        else:
            print("Khong chia duoc cho 0")