"""LAB 7 : SET VÀ  TỪ ĐIỂN DICTIONARY """
# bài 7.1 :
n = int(input("Nhập số N: "))
ket_qua = {} 

for i in range(1, n + 1):
    ket_qua[i] = i * i

print("Từ điển tạo được:", ket_qua)

# bài 7.2 và 7.3:
#  Nhập dữ liệu và xếp loại
sinh_vien = {"An": 8.5, "Bình": 6.0, "Chi": 4.5, "Dũng": 9.0}
xep_loai_sv = {}

for ten, diem in sinh_vien.items():
    if diem >= 8.5: loai = "A"
    elif diem >= 7.0: loai = "B"
    elif diem >= 5.5: loai = "C"
    elif diem >= 4.0: loai = "D"
    else: loai = "F"
    xep_loai_sv[ten] = loai

print("Xếp loại từng bạn:", xep_loai_sv)

#  Đếm tần suất xếp loại
thong_ke = {}
for loai in xep_loai_sv.values():
    thong_ke[loai] = thong_ke.get(loai, 0) + 1

print("Thống kê số lượng theo loại:", thong_ke)


# bài 7.4 và 7.5 :
van_ban = "Python is easy Python is fun"
ds_tu = van_ban.lower().split() 
dem_tu = {}

for tu in ds_tu:
    dem_tu[tu] = dem_tu.get(tu, 0) + 1

print("Số lần xuất hiện:", dem_tu)

#  Tìm từ xuất hiện nhiều/ít nhất
tu_max = max(dem_tu, key=dem_tu.get)
tu_min = min(dem_tu, key=dem_tu.get)
print(f"Từ nhiều nhất: '{tu_max}', Từ ít nhất: '{tu_min}'")

#bài 7.6 và 7.7 :
# Khởi tạo dữ liệu ban đầu
hanh_trang = {
    'vang': 500,
    'tui_nho': ['da_lua', 'day_thung', 'da_quy'],
    'ba_lo': ['dan_go', 'dao_gam', 'tui_ngu', 'o_banh_mi']
}

# 7.6 
# 1. Thêm một ngăn mới tên là 'tui_quan' vào hành trang
hanh_trang['tui_quan'] = ['vo_oc', 'qua_mong_la', 'xo_vai']

# 2. Cộng thêm 50 đơn vị vào lượng 'vang' đang có
hanh_trang['vang'] = hanh_trang['vang'] + 50


#  7.7 ---
#  Sắp xếp lại các món đồ trong 'ba_lo' theo thứ tự bảng chữ cái
hanh_trang['ba_lo'].sort()

# 2. Xóa món đồ 'dao_gam' ra khỏi 'ba_lo'
hanh_trang['ba_lo'].remove('dao_gam')

# In kết quả cuối cùng ra màn hình
print("Hành trang sau khi cập nhật:")
print(hanh_trang)

# bài 7.8 và 7.9 : 
prices = {"apple": 2, "banana": 4, "orange": 1.5}
stock = {"apple": 10, "banana": 6, "orange": 32}

# 7.8: Tính tổng tiền (ví dụ mua mỗi thứ 1 quả)
tong_tien = 0
print("--- HÓA ĐƠN ---")
for hoa_qua in prices:
    gia = prices[hoa_qua]
    so_luong = stock[hoa_qua]
    print(f"{hoa_qua}: {gia}$ (Còn lại: {so_luong})")
    tong_tien += gia

print(f"Tổng cộng: {tong_tien}$")

# 7.9: Khấu trừ kho sau khi mua (ví dụ mua 1 quả mỗi loại)
for hoa_qua in stock:
    stock[hoa_qua] -= 1
print("Kho sau khi bán:", stock)

# bài 7.10 :
kho_hang = {"tivi", "tulanh", "maygiat", "dieuhoa"}
khach_mua = {"tivi", "maygiat"}
chua_mua = kho_hang - khach_mua
print("Các mặt hàng còn trong kho chưa ai mua:", chua_mua)