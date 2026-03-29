n = int(input("Nhap so:"))
s = str(n) #doi so thanh chuoi dung de dao [::-1] va de kiem tra so doi xung
if s == s[::-1]:
    print("la so doi xung")
else:
    print("Khong la so doi xung")