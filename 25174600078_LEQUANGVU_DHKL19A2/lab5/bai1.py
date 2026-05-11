so_nguyen = int(input("Nhap so nguyen duong: "))

nhi_phan = ""

if so_nguyen == 0:
    nhi_phan = "0"

while so_nguyen > 0:
    nhi_phan = str(so_nguyen % 2) + nhi_phan
    so_nguyen = so_nguyen // 2

print("Dang nhi phan:", nhi_phan)