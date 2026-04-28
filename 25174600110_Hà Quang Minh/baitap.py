#vd1
x = 10
def my_function():
    global x
    x = 20
    print(x)
my_function()
print(x)
#vd2
def greet(name,age=30):
    print("Hello,"+name+"!You are "+str(age)+" year old")
greet("Alice")
greet(age=25,name="Alice")
#vd3
def molify_list(lst):
    lst.append(4)
my_list = [1,2,3]
molify_list(my_list)
print(my_list)

#Bài1
def luythua():
    x = int(input('Nhập số x ='))
    n = int(input('Nhập số mũ n ='))
    print('Lũy thừa của ',x,'mũ',n,'=',x**n)
    return 
luythua()

#Bài2
def fibonacci(n): 
    a, b = 0, 1
    print("Dãy Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)

#Bài3
#a
def kt_nt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nhap_so():
    n = int(input("Nhập số nguyên dương n: "))
    return n

n = nhap_so()
if kt_nt(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

#b
def kt_shoanhao(n):
    if n <= 1:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = nhap_so()
if kt_shoanhao(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")

#c
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print('Các số đối xứng trong phạm vi 1000 là:')
dem = 0
for i in range(1, 1000):
    if is_palindrome(i):
        print(str(i).rjust(3), end=" ")
        dem += 1
        if dem % 15 == 0:
            print(' ')

#Bài4
#a
def P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2*i + 1)
    return tich
n = int(input('Nhập n: '))
print('P(n) =', P(n))
#b
def S1(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i if i % 2 != 0 else -i
    return tong
n = int(input('Nhập n: '))
print('S(n) =', S1(n))
#c
def S2(n):
    return (n*(n+1)*(n+2))/6
n = int(input("Nhập n: "))
print("S(n) =", S2(n))
#d
def P(x, y):
    return x ** y
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("P(x,y) =", P(x, y))

#Bài5
import msvcrt
def Ascii():
    print('Nhấn phím bất kỳ để xem giá trị ASCII, nhấn ESC để kết thúc')

    while True:
        char = msvcrt.getch()
        if ord(char)==27:
            break
        print('Giá trị ASCII của ký tự "%s" là%d' % (char.decode(),ord(char)))

Ascii()