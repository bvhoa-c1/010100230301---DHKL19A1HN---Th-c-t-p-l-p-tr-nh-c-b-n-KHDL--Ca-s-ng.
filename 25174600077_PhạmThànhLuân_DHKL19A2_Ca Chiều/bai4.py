#a)
def p(n) :
    tich =1 
    for i in range(n+1):
        tich*=(2*i+1)
    return tich
n= int(input("Nhập n :"))
print(f"p(n) = {p(n)}")

#b)
def s(n) :
    tong =0
    for i in range(1,n+1):
        if i % 2 == 0 :
            tong-=i
        else :
            tong+=i
    return tong
n= int(input("Nhập n :"))
print(f"s(n) = {s(n)}")


#c)
def s(n) :
    tong =0 
    tongg = 0 
    for i in range(n+1):
        tongg+=i
        tong+=tongg
    return tong
n= int(input("Nhập n :"))
print(f"s(n) = {s(n)}")



#d)
def p(x,y) :
    ket_qua =1 
    for i in range(y):
        ket_qua*=x
    return ket_qua
x= int(input("Nhập x :"))
y= int(input("Nhập y :"))
print(f"p(x,y)={p(x,y)}")

