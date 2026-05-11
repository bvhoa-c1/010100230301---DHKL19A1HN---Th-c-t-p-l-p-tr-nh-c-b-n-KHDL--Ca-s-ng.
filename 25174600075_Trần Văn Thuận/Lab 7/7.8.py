so_luong = {
    "táo": 3,
    "cam": 2,
    "bánh": 5
}
don_gia ={
    "táo": 10000,
    "cam": 12000,
    "bánh": 5000
}
tong = 0
print("Hóa đơn")
for mat_hang in so_luong:
    sl = so_luong[mat_hang]
    gia = don_gia[mat_hang]
    thanh_tien = sl * gia
    tong += thanh_tien
    print(mat_hang, ":", sl, "x", gia, "=", thanh_tien)
print("Tổng tiền:", tong)