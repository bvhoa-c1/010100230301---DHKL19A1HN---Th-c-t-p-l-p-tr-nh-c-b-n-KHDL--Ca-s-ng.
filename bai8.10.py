# Nhập danh sách
ds = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

# Lọc số chẵn và tính bình phương
bp_chan = list(map(lambda x: x**2,
                   filter(lambda x: x % 2 == 0, ds)))

# Lọc số lẻ và tính bình phương
bp_le = list(map(lambda x: x**2,
                 filter(lambda x: x % 2 != 0, ds)))

# Xuất kết quả
print("Bình phương số chẵn:", bp_chan)
print("Bình phương số lẻ:", bp_le)