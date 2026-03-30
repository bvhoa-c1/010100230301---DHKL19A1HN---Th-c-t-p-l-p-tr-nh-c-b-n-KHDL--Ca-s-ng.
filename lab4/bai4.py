# Khởi tạo các biến lưu trữ
tong = 0
so_luong = 0
so_lon_nhat = None # Dùng None để xử lý trường hợp chưa có số nào được nhập

print("Nhập các số (nhập 0 để dừng):")

while True:
    n = float(input("Nhập một số: "))
    
    if n == 0:
        break
    
    tong += n
    
    so_luong += 1
    
    if so_lon_nhat is None or n > so_lon_nhat:
        so_lon_nhat = n

if so_luong > 0:
    print("-" * 20)
    print(f"Tổng các số đã nhập: {tong}")
    print(f"Số lượng các số đã nhập: {so_luong}")
    print(f"Số lớn nhất trong các số đã nhập: {so_lon_nhat}")
else:
    print("Bạn chưa nhập số nào ngoài số 0.")