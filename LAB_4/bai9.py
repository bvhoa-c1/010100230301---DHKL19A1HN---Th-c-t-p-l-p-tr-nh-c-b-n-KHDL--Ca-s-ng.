while True:
    print("\n--- MENU ---")
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\n0. Thoát")
    chon = input("Chọn: ")
    if chon == '0': break
    
    a = float(input("Số thứ 1: "))
    b = float(input("Số thứ 2: "))
    
    if chon == '1': print("Kết quả:", a + b)
    elif chon == '2': print("Kết quả:", a - b)
    elif chon == '3': print("Kết quả:", a * b)
    elif chon == '4': print("Kết quả:", a / b if b != 0 else "Lỗi chia cho 0")