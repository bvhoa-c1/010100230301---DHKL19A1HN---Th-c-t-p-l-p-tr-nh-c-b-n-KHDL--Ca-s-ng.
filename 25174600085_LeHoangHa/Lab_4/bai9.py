while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")

    choice = int(input("Chọn: "))

    if choice == 0:
        break

    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    if choice == 1:
        print("Kết quả:", a + b)
    elif choice == 2:
        print("Kết quả:", a - b)
    elif choice == 3:
        print("Kết quả:", a * b)
    elif choice == 4:
        if b != 0:
            print("Kết quả:", a / b)
        else:
            print("Không chia được cho 0")
    else:
        print("Lựa chọn sai")
