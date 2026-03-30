n = int(input("Nhập n: "))

def dem_uoc(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    return count

max_uoc = 0
so = 0

for i in range(1, n+1):
    if dem_uoc(i) > max_uoc:
        max_uoc = dem_uoc(i)
        so = i

print("Số có nhiều ước nhất:", so)