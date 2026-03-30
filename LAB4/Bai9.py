while True:
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    choice = int(input("Chọn: "))
    if choice == 0:
        break
    a = float(input("Số a: "))
    b = float(input("Số b: "))
    if choice == 1:
        print(f"Kết quả: {a + b}")
    elif choice == 2:
        print(f"Kết quả: {a - b}")
    elif choice == 3:
        print(f"Kết quả: {a * b}")
    elif choice == 4:
        if b != 0:
            print(f"Kết quả: {a / b}")
        else:
            print("Không chia được cho 0!")
