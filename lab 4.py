n = int(input("Nhap n: "))

a = 0
b = 1
i = 1

while i < n:
    c = a + b
    a = b
    b = c
    i += 1

print("So Fibonacci thu", n, "la:", a)
#bai2
mk = ""

while mk != "123456":
    mk = input("Nhap mat khau: ")

print("Dang nhap thanh cong")
#bai 3 
n = int(input("Nhap n: "))

i = n - 1

while i > 0:
    if n % i == 0:
        print("Uoc lon nhat:", i)
        break
    i -= 1
#bài 4
tong = 0
dem = 0
max_so = None

while True:
    x = int(input("Nhap so: "))
    
    if x == 0:
        break
        
    tong += x
    dem += 1
    
    if max_so is None or x > max_so:
        max_so = x

print("Tong:", tong)
print("So luong:", dem)
print("So lon nhat:", max_so)
#bài 5
n = int(input("Nhap n: "))

goc = n
dao = 0

while n > 0:
    dao = dao*10 + n%10
    n //= 10

if goc == dao:
    print("La so doi xung")
else:
    print("Khong phai")
    # bài 6
n = int (input("nhập n:"))
tong = 0
s= str(n)
k= len (s)
for i in s:
    tong += int (i)**k
    if tong == n:
        print (" là số amstrong")
    else:
        print(" khong phai số armstrong ")
# bài 7
i = 2
while i <= 9:
    j =1
    while j <= 10:
        print(i, "x",j,"=",i*j)
        j += 1
        print ()
        i+=1
    # bài 8
n = int ( input (" nhập n:"))
tong = 0
tich =1
dao = 0
while n >0:
    so = n%10
    tong += so
    tich *= so
    dao = dao*10 + so
    n //= 10

print("Tong:", tong)
print("Tich:", tich)
print("So dao:", dao)
# bài 9
while True:
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("0. Thoat")
    
    chon = int(input("Chon: "))
    
    if chon == 0:
        break
        
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    
    if chon == 1:
        print(a + b)
    elif chon == 2:
        print(a - b)
    elif chon == 3:
        print(a * b)
    elif chon == 4:
        print(a / b)
        # bài 10
n = 4
while n>0:
    i= 0 
    while i < n:
        print ("*",end = "")
        i += 1
        print ()
        n-=1
    # bài 11 a
    n = int (input(" nhập n(> 10):"))
    a=1 
    S1=0
    while a<= n:
        S1= 6 **a
        a+= 1
        print("S1=", S1)
#b
n = int (input(" nhập n(> 10):"))
a=1 
S2=0
while a<= n:
    S2 +=1/(3**a)

a+= 2
print("S2=", S2)
#c
n = int (input(" nhập n(> 10):"))
a=1 
S3=0
while a<= n:
    S3 +=(-1)**a*a**2

a+= 1
print("S3=", S3)
#d
n = int (input(" nhập n(n>10):"))
a=1
S4=0
while a<= n:
    S4 += a*(a+1)*(a+2)
    a+=1
    print("S4 =",S4)