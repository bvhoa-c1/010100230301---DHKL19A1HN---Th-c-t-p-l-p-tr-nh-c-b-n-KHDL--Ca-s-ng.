while True:
    print("_____MENU_____")
    print("1.Cộng")
    print("2.Trừ")
    print("3.Nhân")
    print("4.Chia")
    print("0.Thoát")

    chon = int(input("Nhập số: "))
    if chon == 0:
        print("Thoát")
        break
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))

    if chon == 1:
        cong = a+b
        print("Kết quả = ",cong)
    elif chon == 2:
        tru = a - b
        print("Kết quả = ",tru)
    elif chon == 3:
        nhan = a*b
        print("Kết quả = ",nhan)
    elif chon == 4:
        if b!=0:
            chia = a/b
            print("Kết quả = ",chia)
        else:
            print("Không có kết quả")
    else:
        print("Lựa chọn không đúng")
print()