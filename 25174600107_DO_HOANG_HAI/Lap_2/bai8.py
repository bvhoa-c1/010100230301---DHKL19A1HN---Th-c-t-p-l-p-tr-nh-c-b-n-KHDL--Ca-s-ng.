n = int(input("Nhap so n: "))

s = str(n)
tong = 0
tich = 1

for i in range(len(s)):
    chu_so = int(s[i])
    tong = tong + chu_so
    tich = tich * chu_so

so_dao = int(s[::-1])

print("Tong cac chu so:", tong)
print("Tich cac chu so:", tich)
print("So dao:", so_dao)
