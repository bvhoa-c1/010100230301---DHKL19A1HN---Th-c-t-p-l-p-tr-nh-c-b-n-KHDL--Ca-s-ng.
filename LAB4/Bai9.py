while True:
    print("\n--- MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    
    chon = input("Chọn chức năng: ")
    
    if chon == '0':
        print("Đã thoát chương trình.")
        break
    elif chon in ['1', '2', '3', '4']:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        
        if chon == '1':
            print(f"Kết quả: {a + b}")
        elif chon == '2':
            print(f"Kết quả: {a - b}")
        elif chon == '3':
            print(f"Kết quả: {a * b}")
        elif chon == '4':
            if b == 0:
                print("Lỗi: Không thể chia cho 0!")
            else:
                print(f"Kết quả: {a / b}")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!")