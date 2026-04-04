n = int(input("Nhap n: "))

s = str(n)
so_chu_so = len(s)

tong = 0
for i in range(so_chu_so):
    chu_so = int(s[i])
    tong = tong + chu_so ** so_chu_so

if tong == n:
    print("Dung, so", n, "la so Armstrong")
else:
    print("Sai, so", n, "khong la so Armstrong")
