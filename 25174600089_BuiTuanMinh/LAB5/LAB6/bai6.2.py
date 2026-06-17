def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def so_hoan_hao(n):
    if n<2 :
        return False
    tong_uoc = sum(i for i in range (1,n) if n % i ==0)
    return tong_uoc== n
n = int(input("nhap n "))
mang= []
for i in range (n):
    x = int(input(i+1))
    mang.append(x)
nguyen_to= [x for x in mang if so_nguyen_to(x)]
hoan_hao= [x for x in mang if so_hoan_hao(x)]
print(nguyen_to)
print(hoan_hao)