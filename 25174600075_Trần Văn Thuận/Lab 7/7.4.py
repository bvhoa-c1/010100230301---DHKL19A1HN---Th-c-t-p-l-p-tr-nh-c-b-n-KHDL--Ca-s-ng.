vb = input("Nhập đoạn văn bản: ")
vb = vb.lower()
for ky_tu in "":
    vb = vb.replace(ky_tu, "")
cac_tu = vb.split()
dem_tu = {}
for tu in cac_tu:
    dem_tu[tu] = dem_tu.get(tu, 0)+ 1
print("số lần xuất hiện: ")
for tu in dem_tu:
    print(tu, ":", dem_tu[tu])