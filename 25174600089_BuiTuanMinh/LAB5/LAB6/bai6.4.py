n = int(input("nhap n:"))
fibonacci = [0,1]
for i in range(2,n):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
fibonacci=fibonacci[:n]
print(fibonacci)