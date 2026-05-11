str = input("Nhập một chuỗi văn bản: ")
k = input("Nhập một từ khóa: ")
vi_tri = str.find(k)
print(f"Vị trí của từ khóa {k} là: {vi_tri}")
tach = str.split()
tu = ''
dem = 0 
for i in tach:
    s = tach.count(i)
    if s > dem:
        dem = s 
        tu = i 
print("Từ xuất hiện nhiều nhất là: ",tu)
print(f"Số lần từ {tu} xuất hiện là: {dem}")