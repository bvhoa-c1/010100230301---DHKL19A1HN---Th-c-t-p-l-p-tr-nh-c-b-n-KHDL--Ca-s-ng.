N = int(input("nhap N:"))
tu_dien={}
for i in range(1,N+1):
    tu_dien[i]=i**3
print("tu dien")
for khoa,gia_tri in tu_dien.items():
    print(khoa,gia_tri)