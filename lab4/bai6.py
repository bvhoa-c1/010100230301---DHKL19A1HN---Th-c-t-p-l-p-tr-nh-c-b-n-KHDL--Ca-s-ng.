# Nhập số n
n_str = input("Nhập số n: ")
n_int = int(n_str)

so_chu_so = len(n_str)

# Khởi tạo tổng
tong_luy_thua = 0
temp = n_int

while temp > 0:
    chu_so = temp % 10 # Lấy chữ số cuối
    tong_luy_thua += chu_so ** so_chu_so # Cộng lũy thừa vào tổng
    temp //= 10 # Loại bỏ chữ số cuối

# Kiểm tra điều kiện
if tong_luy_thua == n_int:
    print(f"{n_int} là số Armstrong.")
else:
    print(f"{n_int} không phải là số Armstrong.")