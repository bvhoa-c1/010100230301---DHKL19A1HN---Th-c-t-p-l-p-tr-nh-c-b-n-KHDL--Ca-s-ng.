while True:
    # Hiển thị Menu
    print("\n---------- MENU MÁY TÍNH ----------")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    print("-----------------------------------")
    
    luon_chon = input("Mời bạn chọn chức năng (0-4): ")
    
    if luon_chon == '0':
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break
    
    # Kiểm tra tính hợp lệ của lựa chọn
    if luon_chon in ['1', '2', '3', '4']:
        # Nhập hai số để thực hiện phép tính
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        
        if luon_chon == '1':
            print(f"Kết quả: {a} + {b} = {a + b}")
        elif luon_chon == '2':
            print(f"Kết quả: {a} - {b} = {a - b}")
        elif luon_chon == '3':
            print(f"Kết quả: {a} * {b} = {a * b}")
        elif luon_chon == '4':
            if b != 0:
                print(f"Kết quả: {a} / {b} = {a / b}")
            else:
                print("Lỗi: Không thể chia cho số 0!")
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại từ 0 đến 4.")