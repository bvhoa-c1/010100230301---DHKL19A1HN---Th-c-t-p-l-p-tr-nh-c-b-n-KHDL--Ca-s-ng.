n = int(input("nhập n: "))
a = n 
so_chu_so = len(str(n))
tong = 0 
while a > 0: 
    chu_so = a % 10 
    tong += chu_so ** so_chu_so
    a //= 10 
if tong == n: 
    print("là số amstrong")
else: 
    print("k là số amstrong")