
#bai1
n = int(input("nhap n: "))
a=0
b=1
while n>0:
    print(a)
    a, b= b, a+b
    n-=1
#bai2 
khoa=int('123456')
mk = int(input("nhap khoa: "))
while True:
    if khoa != mk:
        print("mat khau sai")
        mk = int(input("nhap lai mat khau: "))
    else:
        print("nhap mat khau thanh cong")
        break
#bai3 
n = int(input("nhap so n: "))
ucln = n-1
while ucln>=1:
    if n%ucln == 0:
        print(ucln)
        break
    ucln-=1
#bai4 
tong = 0
dem = 0
somax = None
while True:
    n = int(input("nhap n: "))
    if n == 0:
        print("ket thuc")
        break
    tong+=n
    dem+=1
    if somax is None or n>somax:
        somax=n
print("tong la: ", tong)
print("so dem la: ", dem)
print("so lon nhat la: ", somax if dem > 0 else "khong co so max")
#bai 5
n = input("nhap n: ")
print("la so doi xung" if n == n[::-1] else "khong la so doi xung")
#bai6
n = abs(int(input("nhap n: ")))
goc = n 
a = len(str(n))
armstrong = 0
while n>0:
    b = n%10
    armstrong += b**a
    n //= 10
print("so armstrong" if armstrong == goc else "khong phai so armstrong")
#bai7
print("Bang cuu chuong tu 2 den 9")
m = 2
while m <= 9:
    n = 0
    while n <= 10:
        print(f"{n} x {m} = {m*n}", end='; ')
        n+=1
    print()
    m+=1
#bai8 
n = int(input("nhap n: "))
x = n
tong = 0
tich = 1
sodao = 0
while x > 0:
    du = x%10
    sodao = sodao*10 + du
    x//=10
    tong+=du
    tich*=du
print('tong la: ', tong)
print('tich la: ', tich)
print('so dao la: ', sodao)
#bai 9:                  """
while True:
    print("""1. Cộng
2. Trừ
3. Nhân
4. Chia 
0. Thoát""")
    chon = int(input("Chon chuong trinh trong menu(0-4): "))
    if chon == 1:
        print("a + b")
    elif chon==2:
        print("a - b")
    elif chon==3:
        print("a x b")
    elif chon==4:
        print("a : b")
    elif chon==0:
        print("thoat")
        break
    else:
        print("nhap sai")
#bai 10 
n = int(input("chieu cao: "))
i = n
while i>0:
    j = 1
    while j <=i:
        print("*", end="")
        j+=1
    print()
    i-=1
#bai 11
n = int(input("nhap n: "))
while n <= 10:
    n = int(input("nhap lai n: "))
#a
a=1
s1=0
while a<=n:
    s1+=6**a
    a+=1
print(s1)
#b
a=1
s2=0
while a<=n:
    s2+= 1/(3**(2*a-1))
    a+=1
print(s2)
#c
a=1
s3=0
while a<=n:
    s3+=(((-1)**a)*(a**2))
    a+=1
print(s3)
#d
a=1
s4=0
while a<=n:
    s4+=a*((a+1)*(a+2))
    a+=1
print(s4)




























































































































































































































































































































































