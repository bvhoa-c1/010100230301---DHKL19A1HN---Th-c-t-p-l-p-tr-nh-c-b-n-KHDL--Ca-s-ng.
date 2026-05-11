van_ban = input("Nhập văn bản : ")
tu_khoa = input("Nhập từ khóa : ")
tu = van_ban.split()
print(f"Vị trí xuất hiện của {tu_khoa} : ")
for  i in range(len(tu)) :
    if tu[i] == tu_khoa :
        print(i)
ds = {}
for j in tu :
    ds[j] = ds.get(j,0)+1
x = max(ds.values())
for a,b in ds.items() :
    if b == x :
        print(f"Từ xuất hiện nhiều nhất là {a} - {b} lần")



