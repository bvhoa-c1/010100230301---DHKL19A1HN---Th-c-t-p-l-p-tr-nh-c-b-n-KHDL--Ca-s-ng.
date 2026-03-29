#câu1
#a
tong = 0
for i in range(2000,4001):
    if (i % 7 == 0 and i % 5 != 0):
        tong = tong + i
print(tong)
#b
tong = 0
for i in range (500,1001):
    if (i % 4 ==0 and i % 6 !=0):
        tong = tong + i
print(tong)
#câu2
for i in range(1,10):
    for j in range (1,10):
        print(f"{i}*{j} = {i*j}")
#câu3
n = int(input("nhập vào số hàng của tam giác :"))
for i in range (1,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()
#câu4
#a  tính tổng s1
n = int(input("nhập vào số nguyên dương n:"))
while n <= 0:
    n = int(input("nhập lại n > 0 :"))
tong = 0
for i in range(1,n+1):
    tong  = tong + i
print(tong)
#b tính tổng s2
n = int(input("nhập vào số nguyên dương n:"))
while n <= 0:
    n = int(input("nhập lại n > 0 :"))
tong = 0
for i in range(1,n+1):
    tong = tong + 1/i
print(tong)
#c tinh tong s3
n = int(input("nhập vào số nguyên dương n:"))
while n <= 0:
    n = int(input("nhập lại n > 0 :"))
tong = 0
import math
for i in range(1,n+1):
    tong = tong + 1 / math.sqrt(2*i)
print(tong)
#d tính tổng s4
n = int(input("nhập vào số nguyên dương n:"))
while n <= 0:
    n = int(input("nhập lại n > 0 :"))
tong = 0
import math
for i in range(1,n+1):
    tong = tong + (-1)**(i+1)/i
print(tong)
#câu5
import math
for i in range(1,1001):
    if math.sqrt(i) == int(math.sqrt(i)):
       print(i)
#câu6
n = int(input("nhập vào số nguyên dương n"))
tong_nghich_dao = 0
for i in range(1,n+1):
    tong_nghich_dao = tong_nghich_dao + 1/i
print(tong_nghich_dao)
#câu7
n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    tong = sum(int(ch) for ch in str(i))  
    if tong % 2 == 0:
        dem += 1
print(dem)
#câu8
n = int(input("nhập n"))
for i in range(1,n+1):
    tong = sum(int(ch) for ch in str(i))
#câu9
n = input()
best = n
max_sum = sum(int(c) for c in n)
for i in range(len(n)):
    if n[i] == '0':
        continue
    s = n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
    if sum(int(c) for c in s) > max_sum:
        max_sum = sum(int(c) for c in s)
        best = s
print(best)