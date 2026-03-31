chuoi_n = input("Nhập số n: ")
tong = 0
tich = 1
so_dao = ""

i = 0
while i < len(chuoi_n):
    chu_so = int(chuoi_n[i])
    tong += chu_so
    tich *= chu_so
    
    # Nối chữ số mới vào ĐẦU chuỗi để đảo ngược
    so_dao = str(chu_so) + so_dao 
    i += 1

print(f"- Tổng chữ số: {tong}")
print(f"- Tích chữ số: {tich}")
print(f"- Số đảo: {so_dao}")