tong = 0
dem = 0
so_lon_nhat = float('-inf')  # Khởi tạo số lớn nhất bằng âm vô cực

while True:
    so = float(input("Nhập số (nhập 0 để dừng): "))
    if so == 0:
        break
        
    tong += so
    dem += 1
    
    if so > so_lon_nhat:
        so_lon_nhat = so

if dem > 0:
    print(f"- Tổng các số: {tong}")
    print(f"- Số lượng số đã nhập: {dem}")
    print(f"- Số lớn nhất: {so_lon_nhat}")
else:
    print("Bạn chưa nhập số nào hợp lệ!")