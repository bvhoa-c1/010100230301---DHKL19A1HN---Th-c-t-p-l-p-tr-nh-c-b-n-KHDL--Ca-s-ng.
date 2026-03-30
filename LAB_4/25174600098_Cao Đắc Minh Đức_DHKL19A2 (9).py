while True:
    print("\n1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    choice = int(input("Chọn: "))

    if choice == 0:
        break

    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    if choice == 1:
        print("KQ:", a + b)
    elif choice == 2:
        print("KQ:", a - b)
    elif choice == 3:
        print("KQ:", a * b)
    elif choice == 4:
        if b != 0:
            print("KQ:", a / b)
        else:
            print("Không chia được")