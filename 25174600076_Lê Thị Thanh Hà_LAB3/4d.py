n = 0
while n <= 0:
    n = int(input("Nhập n nguyên dương: "))
# d) S4 = 1/1 - 1/2 + 1/3 - ... + ((-1)^(n+1))/n
s4 = sum(((-1)**(i+1))/i for i in range(1, n + 1))
print(s4)