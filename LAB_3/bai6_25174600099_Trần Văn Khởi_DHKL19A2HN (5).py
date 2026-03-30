#s1 = 1/1 + 1/2 + 1/3 + ... + 1/n
tong = 0
n = int(input("nhập n:"))
for i in range(1,n+1):
    tong +=1/i
print("tổng nghịch đảo là:",tong)