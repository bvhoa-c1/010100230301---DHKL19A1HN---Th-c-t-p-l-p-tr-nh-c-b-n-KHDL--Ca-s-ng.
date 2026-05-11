# Sử dụng Set để quản lý sản phẩm trong kho

# Nhập danh sách sản phẩm trong kho
kho_hang = set()

n = int(input("Nhap so luong san pham trong kho: "))

for i in range(n):
    san_pham = input("Nhap ten san pham: ")
    kho_hang.add(san_pham)

# Nhập danh sách sản phẩm khách đã chọn
khach_chon = set()

m = int(input("Nhap so luong san pham khach da chon: "))

for i in range(m):
    san_pham = input("Nhap ten san pham khach chon: ")
    khach_chon.add(san_pham)

# Tìm sản phẩm còn trong kho nhưng khách chưa chọn
con_lai = kho_hang - khach_chon

# Hiển thị kết quả
print("\nSan pham con trong kho nhung khach chua chon:")

for san_pham in con_lai:
    print(san_pham)