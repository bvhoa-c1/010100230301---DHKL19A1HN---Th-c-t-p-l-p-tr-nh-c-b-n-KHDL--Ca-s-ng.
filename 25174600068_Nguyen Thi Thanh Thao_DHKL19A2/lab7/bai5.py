van_ban = input("Nhap van ban: ")

van_ban = van_ban.lower()

for ky_tu in ",.!?;:":
    van_ban = van_ban.replace(ky_tu, "")

danh_sach_tu = van_ban.split()

tan_suat = {}

for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

tu_nhieu_nhat = max(tan_suat, key=tan_suat.get)
tu_it_nhat = min(tan_suat, key=tan_suat.get)

print("Tu xuat hien nhieu nhat:", tu_nhieu_nhat)
print("Tan suat:", tan_suat[tu_nhieu_nhat])

print("Tu xuat hien it nhat:", tu_it_nhat)
print("Tan suat:", tan_suat[tu_it_nhat])