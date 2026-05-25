n = int(input())
x = ""
while n > 0:
    x = str(n % 2) + x
    n //= 2
print(x)

print(x[::-1])
