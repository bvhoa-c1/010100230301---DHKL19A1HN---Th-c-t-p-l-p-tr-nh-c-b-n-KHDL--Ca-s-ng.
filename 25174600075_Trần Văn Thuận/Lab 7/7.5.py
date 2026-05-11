vb = input("Nhập đoạn văn: ")
vb = vb.lower()
cac_tu = vb.split()
dem = {}
for tu in cac_tu:
    dem[tu] = dem.get(tu, 0) + 1
tu_max = max(dem, key=dem.get)
tu_min = min(dem, key=dem.get)
print("Từ xuất hiện nhiều nhất:", tu_max, ":", dem[tu_max], "lần")
print("Từ xuất hiện ít nhất:", tu_min, ":", dem[tu_min], "lần")
