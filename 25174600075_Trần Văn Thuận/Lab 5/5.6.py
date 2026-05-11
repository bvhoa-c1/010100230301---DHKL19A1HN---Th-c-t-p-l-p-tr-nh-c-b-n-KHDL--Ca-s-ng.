chuoi = input("Nhập chuỗi ký tự: ")
tong = len(chuoi)
ky_tu_dac_biet = {}
for ky_tu in chuoi:
    if not(ky_tu.isalnum()): 
        ky_tu_dac_biet[ky_tu] = ky_tu_dac_biet.get(ky_tu, 0) + 1
print("Các ký tự đặc biệt tìm thấy:")
for ky_tu, so_lan in ky_tu_dac_biet.items():
    ty_le = (so_lan / tong)*100
    print(f"'{ky_tu}':{so_lan} lần ({ty_le:.2f}%)")
