n = int(input())
uoc_max = 0
so_uoc_max = 0
for i in range(1,  n +1):
    dem_uoc = 0
    for j in range(1 , i + 1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc > uoc_max:
        uoc_max = dem_uoc
        so_uoc_max = i
print("so co nhieu uoc nhat :", so_uoc_max , "co", uoc_max, "uoc")
