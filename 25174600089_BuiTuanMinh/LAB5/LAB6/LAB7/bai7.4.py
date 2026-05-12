van_ban= input("nhap van ban tieng anh")
sach=""
for ky_tu in van_ban:
    if ky_tu.isalpha() or ky_tu ==" ":
        sach+= ky_tu.lower()
    else:
        sach+=" "
cac_tu = sach.split()
tan_suat = {}
for tu in cac_tu:
    tan_suat[tu] = tan_suat.get(tu, 0 )+1
for tu, so_lan in sorted(tan_suat.items(),key=lambda x: -x[1]):
    print(tu, so_lan)