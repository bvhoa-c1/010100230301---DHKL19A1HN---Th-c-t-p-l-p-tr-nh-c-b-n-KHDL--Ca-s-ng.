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
tu_nhieu_nhat = max(tan_suat, key= tan_suat.get)
tu_it_nhat= min(tan_suat, key= tan_suat.get)
print(tu_it_nhat,tu_nhieu_nhat)