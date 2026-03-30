tong = 0
dem = 0
max_so = -9999

while True:
    x = int(input("Nhap so (0 dung): "))

    if x == 0:
        break

    tong += x
    dem += 1

    if x > max_so:
        max_so = x

print("Tong =", tong)
print("Dem =", dem)
print("Max =", max_so)