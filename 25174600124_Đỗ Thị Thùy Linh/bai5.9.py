s1 = input("Nhap chuoi ban dau: ")
s2 = input("Nhap chuoi muc tieu: ")

if abs(len(s1) - len(s2)) <= 1:
    print("Co the chuyen doi")
else:
    print("Kho chuyen doi")