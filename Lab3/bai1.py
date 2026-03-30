#a)
tong = 0 
for i in range(2000,4001) :
    if i % 7 ==0 and i %5 != 0 :
        tong+=i
print(f"Tổng các số chia hết cho 7 nhưng không chiia hết cho 5 = {tong}")
#b)
sum = 0
for y in range(500,1001) :
    if y % 4 == 0 and y % 6 != 0 :
        sum+=y
print(f"Tổng các số chia hết cho 4 nhưng không chiia hết cho 6 = {sum}")
    