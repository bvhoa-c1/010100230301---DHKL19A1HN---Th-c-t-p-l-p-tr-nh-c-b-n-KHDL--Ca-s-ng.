van_ban = input("Nhap van ban: ")

van_ban = van_ban.lower()

for ky_tu in ",.!?;:":
    van_ban = van_ban.replace(ky_tu, "")

danh_sach_tu = van_ban.split()

tan_suat = {}

for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print(tan_suat)