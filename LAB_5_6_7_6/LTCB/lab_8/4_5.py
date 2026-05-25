n = int(input())
def xet_so(n):
    n = abs(n) #gttd
    hi = n
    SUM = 0
    while n != 0:
        SUM += (n % 10)**3
        n //= 10
    if SUM == hi:
        print("so amstrong")
    else:
        print("k p so ams")
    return SUM
print("kq")
print(xet_so(n))






