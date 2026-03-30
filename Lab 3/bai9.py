n = int(input("nhập n: "))
max_uoc = 0 
so = 1
for i in range(1, n + 1): 
    dem = 0 
    for j in range(1, n + 1): 
        if i % j == 0: 
            dem += 1 
    if dem > max_uoc:
        max_uoc = dem 
        so = i 
print(so)