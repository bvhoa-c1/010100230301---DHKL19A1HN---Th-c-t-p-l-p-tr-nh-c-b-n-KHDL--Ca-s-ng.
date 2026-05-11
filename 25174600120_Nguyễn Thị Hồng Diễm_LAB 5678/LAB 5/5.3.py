vb = input("Nhap van ban: ")
tu_khoa = input("Nhap tu khoa can tim: ")
vi_tri = vb.find(tu_khoa)
print(f"Vi tri dau tien cua tu khoa: {vi_tri}")
cac_tu = vb.split()
dem_tu = {}
for t in cac_tu:
    t = t.lower().strip() 
    dem_tu[t] = dem_tu.get(t, 0) + 1
tu_max = ""
so_lan_max = 0
for t in dem_tu:
    if dem_tu[t] > so_lan_max:
        so_lan_max = dem_tu[t]
        tu_max = t
print("Tu xuat hien nhieu nhat la:", tu_max, "voi", so_lan_max, "lan.")

