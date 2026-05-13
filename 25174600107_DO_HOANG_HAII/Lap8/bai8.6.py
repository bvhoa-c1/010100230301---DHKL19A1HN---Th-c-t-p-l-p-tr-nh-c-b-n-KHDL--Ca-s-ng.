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

n = int(input("Nhập một số nguyên dương: "))

sum_divisors = sumPdivisors(n)

divisors = []
if n > 1:
    divisors.append(1)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

print(f"Các ước số thực sự của {n}: {sorted(divisors)}")
print(f"Tổng các ước số thực sự: {sum_divisors}")
