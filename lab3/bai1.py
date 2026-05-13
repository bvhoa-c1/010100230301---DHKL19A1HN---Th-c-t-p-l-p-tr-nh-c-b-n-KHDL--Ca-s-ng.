#câu a
print("các số chia hết cho 7 trong khoảng[2000,4001] là:")
for i in range(2000,4001):
    if i%7==0:
       
        print(i,end=" ")
 
#câu b
tong=int()
for i in range(500,1001):
    if i%4==0 and i%6!=0:
        tong+=i
print()
print("tổng các số chia hết cho 4 nhưng không chia hết cho 6 là:",tong)