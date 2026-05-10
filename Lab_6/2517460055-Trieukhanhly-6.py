#6.1
n = int(input())
a = list(map(int, input().split()))
even_sum = 0
odd_sum = 0
for x in a:
    if x % 2 == 0:
        even_sum += x
    else:
        odd_sum += x
print("Tổng chẵn:", even_sum)
print("Tổng lẻ:", odd_sum)
#6.2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
a = list(map(int, input().split()))
for x in a:
    if is_prime(x) or is_perfect(x):
        print(x)
#6.3
day_so = input("Nhập dãy số: ").split()
day_so = [float(x) for x in day_so]
lon_nhat = max(day_so)
nho_nhat = min(day_so)
print("Giá trị lớn nhất là:", lon_nhat)
print("Giá trị nhỏ nhất là:", nho_nhat)
#6.4
n = int(input())
fib = [0,1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
print(fib[:n])
#6.5
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
primes = [x for x in range(100) if prime(x)]
print(primes)
#6.6
a = list(map(int, input().split()))
d = a[1] - a[0]
ok = True
for i in range(1, len(a)-1):
    if a[i+1] - a[i] != d:
        ok = False
        break
if ok:
    print("La cap so cong")
else:
    print("Khong phai cap so cong")
#6.7
m = int(input())
n = int(input())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
total = 0
for row in matrix:
    total += sum(row)
print(total)
#6.8
m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
p, q = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(p)]
if n != p:
    print("Khong nhan duoc")
else:
    C = [[0]*q for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    for row in C:
        print(*row)
#6.9
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
AT = [[A[j][i] for j in range(n)] for i in range(n)]
for row in AT:
    print(*row)
print("Doi xung" if A == AT else "Khong doi xung")
#6.10
n = int(input())
A = [list(map(float, input().split())) for _ in range(n)]
I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    if A[i][i] == 0:
        print("Khong kha nghich")
        exit()
    k = A[i][i]
    for j in range(n):
        A[i][j] /= k
        I[i][j] /= k
    for r in range(n):
        if r != i:
            t = A[r][i]
            for j in range(n):
                A[r][j] -= t * A[i][j]
                I[r][j] -= t * I[i][j]
print("Ma tran nghich dao:")
for row in I:
    print(*row)
