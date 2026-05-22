sv = {}
thong_ke = {}
n = int(input())
for i in range(1, (n +1)):
    ten = input()
    diem = float(input())

    if diem >= 8.5:
        loai = "A"
    elif diem >= 7:
        loai = "B"
    elif diem >= 5.5:
        loai = "C"
    else:
        loai = "F"
    sv[ten] = loai
print(sv)
for loai in sv.values():
    if loai in thong_ke:
        thong_ke[loai] += 1
    else:
        thong_ke[loai] = 1
print("thong ke hs" , thong_ke)