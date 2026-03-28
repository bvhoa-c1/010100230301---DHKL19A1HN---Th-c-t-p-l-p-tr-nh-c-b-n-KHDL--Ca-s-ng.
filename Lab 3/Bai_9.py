n = int(input("Nhập n: "))
max_uoc = -1
so_nhieu_uoc_nhat = -1

for i in range(1, n + 1):
    dem_uoc = 0
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            dem_uoc += 1
            if j != i // j:
                dem_uoc += 1
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc_nhat = i
        
print("Số có nhiều ước nhất:", so_nhieu_uoc_nhat)