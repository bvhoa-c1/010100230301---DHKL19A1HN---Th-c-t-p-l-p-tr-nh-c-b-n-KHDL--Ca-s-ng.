#bài 8.1
def is_prime(n):

    if n<2:
        return False

    for i in range(2,int(n**0.5)+1):

        if n%i==0:
            return False

    return True


for i in range(2,1000):

    if is_prime(i) and is_prime(i+2):

        print(i,i+2)

#bài 8.2
def factorial(n):

    s=1

    for i in range(1,n+1):
        s*=i

    return s


print(factorial(5))

#bài 8.3
def P(n,r):

    return factorial(n)//factorial(n-r)


def C(n,r):

    return factorial(n)//(factorial(r)*factorial(n-r))

#bài 8.4
def cubesum(n):

    s=0

    for digit in str(n):

        s+=int(digit)**3

    return s

#bài 8.5
def cubesum(n):

    s = 0

    for digit in str(n):

        s += int(digit) ** 3

    return s


def is_armstrong(n):

    return cubesum(n) == n


print("Cac so Armstrong <1000:")

for i in range(1000):

    if is_armstrong(i):

        print(i, end=" ")

#bài 8.6
def sumPdivisors(n):

    tong = 0


    for i in range(1, n):

        if n % i == 0:

            tong += i


    return tong


n = int(input("Nhap n: "))

print(
    "Tong uoc =",
    sumPdivisors(n)
)

#bài 8.7
def sumPdivisors(n):

    tong = 0


    for i in range(1, n):

        if n % i == 0:

            tong += i


    return tong


def is_amicable(a, b):

    if (
        sumPdivisors(a) == b
        and
        sumPdivisors(b) == a
    ):

        return True


    return False


a = int(input("Nhap a: "))
b = int(input("Nhap b: "))


if is_amicable(a, b):

    print("La cap amicable")

else:

    print("Khong phai")

#bài 8.8
a = list(
    map(
        int,
        input("Nhap day so: ").split()
    )
)


chan = list(
    filter(
        lambda x: x % 2 == 0,
        a
    )
)


le = list(
    filter(
        lambda x: x % 2 != 0,
        a
    )
)


print("So chan:", chan)
print("So le:", le)

#bài 8.9
a = list(
    map(
        int,
        input("Nhap day so: ").split()
    )
)


result = list(

    map(

        lambda x: x**3,

        a
    )
)


print(result)

#bài 8.10
a = list(
    map(
        int,
        input("Nhap day so: ").split()
    )
)


chan = list(

    filter(

        lambda x: x % 2 == 0,

        a
    )
)


le = list(

    filter(

        lambda x: x % 2 != 0,

        a
    )
)


cube_even = list(

    map(

        lambda x: x**3,

        chan
    )
)


square_odd = list(

    map(

        lambda x: x**2,

        le
    )
)


print("Lap phuong so chan:")
print(cube_even)


print("Binh phuong so le:")
print(square_odd)
