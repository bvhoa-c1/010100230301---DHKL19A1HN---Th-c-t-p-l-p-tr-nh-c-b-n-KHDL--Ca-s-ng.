while True:
    print("\n1. Cộng")
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
        print("KQ:", a + b)
    elif chon == 2:
        print("KQ:", a - b)
    elif chon == 3:
        print("KQ:", a * b)
    elif chon == 4:
        if b != 0:
            print("KQ:", a / b)
        else:
            print("Không chia được")