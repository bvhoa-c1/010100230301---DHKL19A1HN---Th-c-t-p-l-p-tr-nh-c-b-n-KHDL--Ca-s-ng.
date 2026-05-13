def cubesum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total

def isArmstrong(n):
    return n == cubesum(n)

armstrong_numbers = []

for num in range(1, 10000):
    if isArmstrong(num):
        armstrong_numbers.append(num)

print("Các số Armstrong nhỏ hơn 10000:")
print(armstrong_numbers)

n = int(input("\nNhập một số để kiểm tra: "))

if isArmstrong(n):
    print(f"{n} là số Armstrong")
else:
    print(f"{n} không phải là số Armstrong")
