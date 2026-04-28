#a,
def so_ngto(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input("Nhập n: "))
if so_ngto(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải số nguyên tố")
#b,
def so_hoan_hao(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s += i
    return s == n
if so_hoan_hao(n):
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")
#c,
def so_doi_xung(n):
    return str(n) == str(n)[::-1]
s = 0 
for i in range (1,1001):
    if so_doi_xung(i):
        print(f"{i:5}",end=" ")
        s += 1
        if s % 15 == 0:
            print()