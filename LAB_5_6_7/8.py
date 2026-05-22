chuoi = input()

if len(chuoi) < 10:
    exit()
a = chuoi[2:9]
b = chuoi[5:10]
c = chuoi[-3:]
a, b, c = map(str.upper, [a, b, c])
print("viet hoa", a , b , c)
a, b , c = map(str.lower , [a, b, c])
print("chu thuong" , a , b , c)
a , b , c = map(str.swapcase, [a, b, c])
print("dao", a , b, c)

