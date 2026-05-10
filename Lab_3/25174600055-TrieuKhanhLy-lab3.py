
#bai1
#a
tong = 0
for i in range(2000, 4000 +1):
    if i%7 == 0 and i % 5!= 0:
        tong += i
print(tong)
#b
t = 0
for i in range(500, 1000 +1):
    if i%4 == 0 and i%6!= 0:
        t += i
print(t)
#bai2 
print("Bang cuu chuong tu 1 den 9")
for i in range(1, 10):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
#bai3 
n = int(input("so hang: "))
for i in range(1, n +1):
    for j in range(1, i +1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#bai4 
n = int(input("nhap n: "))
for _ in range(1000000):
    if n > 0:
        break
    n = int(input("nhap lai n: "))
#a
s1 = 0
for i in range(1, n+1):
    s1+=i
print('s1= ',s1)
#b
s2 = 0
for i in range(1, n+1):
    s2+=1/i
print('s2= ',s2)
#c
s3=0
for i in range(1, n+1):
    s3=1/((2*i)**(0.5))
print('s3= ',s3)
#d
s4=0
for i in range(1, n+1):
    if i%2==1:
        s4+=((-1)**(i+1))/i
    else:
        s4-=((-1)**(i+1))/i
print('s4=',s4)
#bai5
for i in range(1,int(1000**0.5)+1):
    print(i*i)
#bai 6
n = int(input("n: "))
s1 = 0
for i in range(1, n+1):
    s1+=1/i
print('s1= ',s1)
#bai 7 
n = int(input("n: "))
dem = 0
for i in range(1, n+1):
    tong = 0
    for j in str(i):
        tong+=int(j)
    if tong%2==0:
        dem+=1
print('so luong: ',dem)
#bai 8
n = int(input("nhap n: "))
somax = 1
tongmax = 0
for i in range(1, n+1):
    tong = 0
    for ch in str(i):
        tong += int(ch)
    if tong > tongmax:
        tongmax= tong
        somax = i
print("so co tong chu so lon nhat la: ", somax)
#bai 9 
n = int(input("nhap n: "))
so=0
souoc=0
for i in range(1, n+1):
    dem=0
    for j in range(1, i+1):
        if i%j==0:
            dem+=1
    if dem>souoc:
        souoc=dem
        so=i
print('so co nhieu uoc nhat la: ',so) 
#ba11 
n = int(input("nhap n: "))
a=0
b=1
for i in range(1, n+1):
    print(a)
    c=a+b
    a, b=b, c
#bai 12
container = input("Nhập mã container 10 ký tự: ")

bang_ma = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18,
    'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27,
    'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36,
    'Y': 37, 'Z': 38
}
tong = 0
for i in range(len(container)):
    ky_tu = container[i]
    if 'A' <= ky_tu <= 'Z':
        gia_tri = bang_ma[ky_tu]
    else:
        gia_tri = int(ky_tu)
    tong += gia_tri * (2 ** i)
check_digit = tong % 11
if check_digit == 10:
    check_digit = 0
print("Số kiểm tra container là:", check_digit)
















