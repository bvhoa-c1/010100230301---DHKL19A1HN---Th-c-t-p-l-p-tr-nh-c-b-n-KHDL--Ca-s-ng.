tong = 0
dem = 0
max_so = None

while True:
    n = int(input("Nhap so 0 de dung:"))
    if n == 0:
        break
    tong +=n
    dem += 1
    if max_so is None or n > max_so:
        max_so = n
print(tong)
print(dem)
print(max_so)