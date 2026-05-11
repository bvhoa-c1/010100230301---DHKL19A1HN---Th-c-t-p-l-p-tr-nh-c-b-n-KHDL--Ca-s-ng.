# lập phương của các phần tử trong danh sách

# Nhập danh sách số
ds = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

# Tính lập phương bằng map
lap_phuong = list(map(lambda x: x**3, ds))

# Xuất kết quả
print("Danh sách lập phương:", lap_phuong)