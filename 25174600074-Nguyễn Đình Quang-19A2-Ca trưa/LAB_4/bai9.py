while True:
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = int(input("Chọn: "))

    if chon == 0:
        break

    a = float(input("a = "))
    b = float(input("b = "))

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