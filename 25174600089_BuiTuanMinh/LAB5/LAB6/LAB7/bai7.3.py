def xep_loai(diem):
    if diem>=90: return 'A'
    elif diem>=80: return 'B'
    elif diem>=70: return'C'
    elif diem>=60: return'D'
    elif diem>=50: return'E'
    else: return 'F'
n = int(input("nhap so sihn vien"))
tan_suat= {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
for tan_suat in range(n):
    ten = input("nhap ten")
    diem = float(input("nhap diem"))
    loai= xep_loai
    tan_suat[loai]+=1
print("bao cao")
for loai, so_luong in tan_suat.items():
    print(loai,tan_suat)