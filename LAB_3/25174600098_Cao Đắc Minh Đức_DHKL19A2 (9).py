def dem_uoc(k):
    count = 0
    for i in range(1, int(k**0.5) + 1):
        if k % i == 0:
            if i*i == k:
                count += 1
            else:
                count += 2
    return count

n = int(input("Nhập n: "))

so_nhieu_uoc_nhat = 1
max_uoc = 0

for i in range(1, n + 1):
    so_uoc_hien_tai = dem_uoc(i)
    if so_uoc_hien_tai > max_uoc:
        max_uoc = so_uoc_hien_tai
        so_nhieu_uoc_nhat = i

print(f"Số có nhiều ước nhất là {so_nhieu_uoc_nhat} với {max_uoc} ước.")


