def sumPdivisors(n):
    if n <= 1:
        return 0
    
    total = 1
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    
    return total

def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if isAmicable(a, b):
    print(f"{a} và {b} là cặp số Amicable")
else:
    print(f"{a} và {b} không phải là cặp số Amicable")

print(f"\nTổng ước số của {a}: {sumPdivisors(a)}")
print(f"Tổng ước số của {b}: {sumPdivisors(b)}")

print("\nCác cặp số Amicable nhỏ hơn 2000:")
amicable_pairs = []
for num in range(1, 2000):
    if isAmicable(num, sumPdivisors(num)):
        pair = tuple(sorted([num, sumPdivisors(num)]))
        if pair not in amicable_pairs:
            amicable_pairs.append(pair)

for pair in amicable_pairs:
    print(pair)
