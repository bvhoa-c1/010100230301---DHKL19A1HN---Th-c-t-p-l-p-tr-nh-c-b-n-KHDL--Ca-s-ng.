while True:
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    choice = input("Chọn phép toán: ")
    
    if choice == '0':
        break
    elif choice in ['1', '2', '3', '4']:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        if choice == '1':
            print(a + b)
        elif choice == '2':
            print(a - b)
        elif choice == '3':
            print(a * b)
        elif choice == '4':
            if b != 0:
                print(a / b)
            else:
                print("Lỗi chia 0")