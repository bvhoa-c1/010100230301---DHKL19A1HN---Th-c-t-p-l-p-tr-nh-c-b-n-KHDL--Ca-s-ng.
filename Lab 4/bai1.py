n = int(input("nhập n: "))
a = 0
b = 1
i = 1 
while i < n: 
    a = b
    b = a + b 
    i += 1 
print("số fibonacci thứ ", n ,"là", a)