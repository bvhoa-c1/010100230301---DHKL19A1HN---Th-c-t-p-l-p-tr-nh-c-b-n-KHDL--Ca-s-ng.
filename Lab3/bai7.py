n = int(input("Nhập n : "))
dem = 0
for i in range(1,n+1) :
    tong = 0 
    for x in str(i) :
        tong+=int(x)
    if tong % 2 == 0 :
        dem +=1
print(f"Số lượng số trong khoảng từ 1 đến {n} có tổng chữ số là số chẵn là {dem} số")
