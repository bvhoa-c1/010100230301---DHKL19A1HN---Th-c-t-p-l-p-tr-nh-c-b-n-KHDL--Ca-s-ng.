while True:
    print("===== MENU =====")
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Thoat")
    
    chon = int(input("Chon chuc nang: "))
    
    if chon == 0:
        print("Tam biet!")
        break
    
    if chon == 1 or chon == 2 or chon == 3 or chon == 4:
        a = float(input("Nhap so thu nhat: "))
        b = float(input("Nhap so thu hai: "))
        
        if chon == 1:
            print("Ket qua:", a + b)
        elif chon == 2:
            print("Ket qua:", a - b)
        elif chon == 3:
            print("Ket qua:", a * b)
        elif chon == 4:
            if b == 0:
                print("Khong the chia cho 0")
            else:
                print("Ket qua:", a / b)
    else:
        print("Lua chon khong hop le")
    
    print()
