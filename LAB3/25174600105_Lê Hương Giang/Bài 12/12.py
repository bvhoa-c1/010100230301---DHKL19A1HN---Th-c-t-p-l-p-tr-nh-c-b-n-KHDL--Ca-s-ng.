s = input("Nhập mã: ")

tong = 0

for i in range(len(s)):
    if s[i].isalpha():   # nếu là chữ
        gia_tri = ord(s[i]) - 55
        if gia_tri >= 11:
            gia_tri += 1   # bỏ số 11
    else:   # nếu là số
        gia_tri = int(s[i])
    
    tong += gia_tri * (2 ** i)

kq = tong % 11
if kq == 10:
    kq = 0

print(kq)