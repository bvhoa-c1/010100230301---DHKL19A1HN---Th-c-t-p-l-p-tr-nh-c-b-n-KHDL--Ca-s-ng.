def dem_uoc(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

n = int(input("Nhap n: "))
max_uoc = 0
res = 1

for i in range(1, n + 1):
    u = dem_uoc(i)
    if u > max_uoc:
        max_uoc = u
        res = i

print("So =", res, "co", max_uoc, "uoc")