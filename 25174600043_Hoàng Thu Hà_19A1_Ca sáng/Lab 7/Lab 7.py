# Bài 7.1: Nhập số nguyên N, khởi tạo một từ điển có kích thước N với khóa là x và giá trị tương ứng được tính bằng x3
N = int(input("Nhập N: "))
d = {}
for x in range(1, N+1):
    d[x] = x**3
print("Từ điển và giá trị tương ứng là:")
print(d)


# Bài 7.2: Xây dựng từ điển lưu trữ thông tin tên và điểm thi của sinh viên. Thực hiện thuật toán ánh xạ điểm số sang các mức xếp loại học thuật chuẩn từ A đến F
n = int(input("Nhập số lượng sinh viên: "))
sinhvien  = {}
for i in range(n):
    ten = input(f"Nhập tên sv thứ {i+1}: ")
    diem = float(input(f"Nhập điểm sv thứ {i+1}: "))

    if diem >= 8.5:
        xeploai = "A"
    elif diem >= 7:
        xeploai = "B"
    elif diem >= 5.5:
        xeploai = "C"
    elif diem >= 4:
        xeploai = "D"
    else:
        xeploai = "F"

    sinhvien[ten] ={
        "Điểm": diem,
        "Xếp loại": xeploai
    }
print("\nDanh sách sinh viên:")
for ten, thongtin in sinhvien.items():
    print(ten, ":", thongtin)


# Bài 7.3: Dựa trên từ điển dữ liệu sinh viên đã phân loại, thiết lập một từ điển đếm tần suất
# để báo cáo số lượng sinh viên đạt được ở từng mức học lực.
dem = {}
for thongtin in sinhvien.values():
    xeploai = thongtin["Xếp loại"]
    if xeploai in dem:
        dem[xeploai] += 1
    else:
        dem[xeploai] = 1
print(dem)


# Bài 7.4: Khảo sát một đoạn văn bản tiếng Anh. Xử lý làm sạch chuỗi và sử dụng cấu trúc
# từ điển để lưu trữ số lần xuất hiện của từng từ vựng riêng biệt
vanban = input("Nhập đoạn văn bản tiếng Anh: ")
vanban = vanban.lower()
for dau in ",.!?;:":
    vanban = vanban.replace(dau, "")
tudon = vanban.split()

dem = {}
for tu in tudon:
    if tu in dem:
        dem[tu] += 1
    else:
        dem[tu] = 1

print("Số lần xuất hiện của từng từ:")
for tu, soluong in dem.items():
    print(tu, ":", soluong)


# Bài 7.5: Tiếp nối dữ liệu từ điển ở bài phân tích văn bản, xây dựng thuật toán duyệt để tìm
# kiếm và xuất ra các từ có tần suất xuất hiện cao nhất và thấp nhất
max_dem = max(dem.values())
min_dem = min(dem.values())

print("Từ xuất hiện nhiều nhất:")
for tu, soluong in dem.items():
    if soluong == max_dem:
        print(tu, ":", soluong)

print("Từ xuất hiện ít nhất:")
for tu, soluong in dem.items():
    if soluong == min_dem:
        print(tu, ":", soluong)


# Bài 7.6: Thao tác trên từ điển quản lý hành trang (Inventory). Bổ sung trường dữ liệu mới
# (khóa pocket chứa danh sách vật phẩm) và cập nhật số lượng cho khóa gold
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["gold"] += 50
print("Inventory sau khi cập nhật:")
for key, value in inventory.items():
    print(key, ":", value)


# Bài 7.7: Thực hiện sắp xếp theo thứ tự từ điển cho danh sách các vật phẩm nằm trong khóa
# backpack và loại bỏ một vật phẩm cụ thể khỏi danh sách này
inventory = {
    "gold": 550,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"],
    "pocket": ["seashell", "strange berry", "lint"]
}
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
print("Backpack sau khi cập nhật:")
print(inventory["backpack"])


# Bài 7.8: Vận dụng hai từ điển biểu diễn thông tin số lượng tồn kho và đơn giá. Tính toán
# chi phí, định dạng và in hóa đơn chi tiết cho các mặt hàng
soluong = {
    "Táo": 3,
    "Cam": 2,
    "Sữa": 1
}
dongia = {
    "Táo": 15000,
    "Cam": 20000,
    "Sữa": 30000
}
tong = 0
print("===== HÓA ĐƠN =====")

for mathang in soluong:
    sl = soluong[mathang]
    gia = dongia[mathang]
    thanhtien = sl * gia
    tong += thanhtien

    print(mathang)
    print("Số lượng:", sl)
    print("Đơn giá:", gia)
    print("Thành tiền:", thanhtien)
    print()
print("Tổng hóa đơn:", tong)


# Bài 7.9: Phát triển thủ tục khấu trừ số lượng vật phẩm đã giao dịch thành công và xuất ra
# báo cáo tình trạng số lượng tồn kho cập nhật của cửa hàng
tonkho = {
    "Táo": 10,
    "Cam": 8,
    "Sữa": 5
}
giaodich = {
    "Táo": 3,
    "Cam": 2
}
for mathang in giaodich:
    tonkho[mathang] -= giaodich[mathang]
print("===== TỒN KHO SAU GIAO DỊCH =====")

for mathang, soluong in tonkho.items():
    print(mathang, ":", soluong)


# Bài 7.10: Vận dụng cấu trúc Set để biểu diễn danh mục sản phẩm của kho hàng. Sử dụng phép toán tập hợp để trích xuất
# các mặt hàng có trong kho nhưng chưa được khách hàng chọn mua.
khohang = {"Táo", "Cam", "Sữa", "Bánh", "Nước"}
khachmua = {"Táo", "Sữa"}
chuamua = khohang - khachmua
print("Các mặt hàng còn trong kho chưa được khách chọn mua:")

for mathang in chuamua:
    print(mathang)

    