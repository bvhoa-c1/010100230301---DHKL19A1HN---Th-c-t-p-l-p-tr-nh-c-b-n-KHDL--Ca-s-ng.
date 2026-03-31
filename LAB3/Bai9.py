n = int(input("\nNhập n: "))
max_uoc = 0
so_nhieu_uoc = 0

for i in range(1, n + 1):
    dem_uoc = 0
    # Đếm xem số i có bao nhiêu ước
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
            
    if dem_uoc > max_uoc:
        max_uoc = dem_uoc
        so_nhieu_uoc = i
        
print(f"Số có nhiều ước nhất là {so_nhieu_uoc} (Có {max_uoc} ước)")