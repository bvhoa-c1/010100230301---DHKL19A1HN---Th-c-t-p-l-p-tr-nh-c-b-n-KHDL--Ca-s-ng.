def xep_loai(diem):
    if diem>=90: return 'A'
    elif diem>=80: return 'B'
    elif diem>=70: return'C'
    elif diem>=60: return'D'
    elif diem>=50: return'E'
    else: return 'F'
n= int(input("nhap so sinh vien"))
sinh_vien={}
for sinh_vien in range(n):
    ten= input("ten sinh vien la:")
    diem= float(input("diem  cua sinh vien la:"))
    sinh_vien[ten]= diem
print(xep_loai)
