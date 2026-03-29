while True:
    print("\n--- MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    
    choice = int(input("Chọn chức năng: "))
    
    if choice == 0:
        print("Thoát chương trình!")
        break
    
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    
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
            print("Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ!")