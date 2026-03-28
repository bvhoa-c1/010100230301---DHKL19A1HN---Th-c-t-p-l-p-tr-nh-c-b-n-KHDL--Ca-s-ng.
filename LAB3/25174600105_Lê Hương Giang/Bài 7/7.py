n = int(input("Nhập số n: "))
dem = 0

for i in range(1,n+1):
    tong_chu_so_chan = 0
    for j in str(i):
        tong_chu_so_chan += int(j)

    if tong_chu_so_chan%2 == 0:
        dem += 1
print("Kết quả = ",dem)