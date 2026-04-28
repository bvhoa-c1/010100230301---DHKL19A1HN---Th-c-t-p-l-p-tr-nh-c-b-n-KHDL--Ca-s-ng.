n = int(input("Nhập n: "))
ULN = 0
so_max = 0
for i in range(1, n+1):
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem += 1
    if dem > ULN:
        ULN = dem
        so_max = i
print("Số:", so_max, "Có", ULN, "ước")