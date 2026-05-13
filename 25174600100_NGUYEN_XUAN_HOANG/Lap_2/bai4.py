tong = 0
dem = 0
max_so = 0

while True:
    so = int(input("Nhap so: "))
    if so == 0:
        break
    tong = tong + so
    dem = dem + 1
    if so > max_so:
        max_so = so

print("Tong cac so:", tong)
print("So luong so:", dem)
print("So lon nhat:", max_so)
