def gia_tri(c):
    if c.isdigit():
        return int(c)
    return ord(c) - ord('A') + 10

container = input("Nhập container: ").strip()

tong = 0
for i in range(len(container)):
    tong += gia_tri(container[i]) * (2 ** i)

check = tong % 11
if check == 10:
    check = 0

print("Check digit:", check)