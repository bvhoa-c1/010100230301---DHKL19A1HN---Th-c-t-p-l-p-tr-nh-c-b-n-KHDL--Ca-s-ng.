n= int(input("Nhập n : "))
tong_uoc = 0 
so = 0 
for i in range(1,n+1) :
    sum = 0 
    for j in range(1,i+1) :
        if i % j == 0 :
            sum+=1 
    if sum > tong_uoc :
        tong_uoc = sum 
        so = i
print("Số có nhiều ước nhất =", so)