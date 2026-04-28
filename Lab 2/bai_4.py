tong = 0
dem = 0
max_val = None

while True:
    x = int(input("Nhap so (0 de dung): "))
    if x == 0:
        break
    
    tong += x
    dem += 1
    
    if max_val is None or x > max_val:
        max_val = x

print("Tong =", tong)
print("So luong =", dem)
print("So lon nhat =", max_val)