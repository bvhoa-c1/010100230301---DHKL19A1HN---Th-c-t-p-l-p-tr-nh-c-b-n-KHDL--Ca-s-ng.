chuoi=  input("nhap chuoi van ban:")
tu_khoa=input("nhap tu khoa can tim:")

vi_tri=[]
bat_dau=0
while True:
    id = chuoi.find(tu_khoa,bat_dau)
    if id == -1:
        break
    vi_tri.append(id)
    bat_dau= id  +1
if vi_tri:
    print(tu_khoa,"xuat hien tai:",vi_tri)
else:
    print(tu_khoa,"ko xuat hien trong chuoi")

tan_suat= {}
for ky_tu in chuoi:
    tan_suat[ky_tu]= tan_suat.get(ky_tu, 0)+1
ky_tu_nhieu_nhat= max(tan_suat, key=tan_suat.get)
print(ky_tu_nhieu_nhat)