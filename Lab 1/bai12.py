def gia_tri_ky_tu(c):
    if c.isalpha():
        return ord(c) - ord('A') + 10
    return int(c)

container = input("Nhap container (10 ky tu): ")

tong = 0

for i in range(10):
    value = gia_tri_ky_tu(container[i])
    tong += value * (2 ** i)

check = tong % 11
if check == 10:
    check = 0

print("So kiem tra =", check)