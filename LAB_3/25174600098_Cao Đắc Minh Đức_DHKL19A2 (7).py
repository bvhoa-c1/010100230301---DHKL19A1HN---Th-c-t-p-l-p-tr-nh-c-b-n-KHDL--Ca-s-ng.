tong=0
n = int(input("nhập n:"))
for i in range(1,n+1):
    tong +=1
    if tong % 2 == 0:
        print("đếm tổng chữ số trong khoảng(1,n) có tổng chữ số là số chẵn:",tong)