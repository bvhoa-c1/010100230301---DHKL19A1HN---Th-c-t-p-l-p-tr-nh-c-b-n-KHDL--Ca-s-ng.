chuoi_n = input("Nhập số n: ")
chuoi_dao = ""

# Lấy chỉ mục phần tử cuối cùng
i = len(chuoi_n) - 1

# Duyệt ngược từ cuối về đầu để nối thành chuỗi đảo
while i >= 0:
    chuoi_dao += chuoi_n[i]
    i -= 1
    
if chuoi_n == chuoi_dao:
    print(f"{chuoi_n} -> đúng")
else:
    print(f"{chuoi_n} -> sai")