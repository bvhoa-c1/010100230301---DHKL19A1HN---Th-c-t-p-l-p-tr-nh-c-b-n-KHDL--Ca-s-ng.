while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    if chon == 0:
        break

    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    if chon == 1:
        print(a + b)
    elif chon == 2:
        print(a - b)
    elif chon == 3:
        print(a * b)
    elif chon == 4:
        if b != 0:
            print(a / b)
        else:
            print("Không chia được")