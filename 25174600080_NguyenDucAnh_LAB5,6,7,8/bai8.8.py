# để tách số chẵn và số lẻ trong danh sách

# Nhập danh sách
ds = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

# Lọc số chẵn
so_chan = list(filter(lambda x: x % 2 == 0, ds))

# Lọc số lẻ
so_le = list(filter(lambda x: x % 2 != 0, ds))

# Xuất kết quả
print("Danh sách số chẵn:", so_chan)
print("Danh sách số lẻ:", so_le)