a = float(int(input("Nhap a:")))
b = float(int(input("Nhap b:")))
while True:
    print("\n=====MENU=====")
    print("1.Cong")
    print("2.Tru")
    print("3.Nhan")
    print("4.Chia")
    print("5.Thoat")

    chon = int(input("Vui long chon:"))

    if chon == 5:
        print("Thoat khoi chuong trinh")
        break
    
    if chon == 1:
        print("Phep cong la:",a + b)
    elif chon == 2:
        print("Phep tru la :",a - b)
    elif chon == 3:
        print("Phep nhan la:",a * b)
    elif chon == 4:
        if b != 0:
            print("Phep chia la :",a / b)
        else:
            print("Error")
    else:
        print("Khong hop le,vui long nhap lai!")
        break
