#bài 1a
tong = 0
for i in range(2000,4001):
    if i%7==0 and i%5!=0:
        tong+=i
print("tổng các số là :",tong)        
# bài 1b
tong = 0
for i in range(500,1001):
    if i%4==0 and i%6!=0:
        tong+=i
print("tổng các số là :",tong)
# bài 2 
n = int(input(" bảng cửu chương bạn cần là : "))
print("bảng cửu chương ",n)
for i in range(1,11):print(" ",n,'x',i,'=',n*i)
# bài 3
n = int(input("Nhập số hàng: "))
for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("*" * n)
    else:
        print("*" + " " * (i - 2) + "*")
# bài 4a 
n = int(input("nhập vào 1 só nguyên : "))
tong = 0
for i in range(1,n+1):
    if n<=0 :print("nhập lại")
    else: tong+=i
print("tổng =",tong)    
    