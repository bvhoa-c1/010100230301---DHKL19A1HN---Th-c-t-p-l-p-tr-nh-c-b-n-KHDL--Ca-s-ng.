# a) 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# b)
def is_perfect(n):
    if n <= 0:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


# c) 
def is_palindrome(n):
    return str(n) == str(n)[::-1]



n = int(input("Nhập số nguyên dương n: "))

# a)
if is_prime(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

# b)
if is_perfect(n):
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")

# c) 
print("\nCác số đối xứng <= 1000:")

count = 0
for i in range(1, 1001):
    if is_palindrome(i):
        print(f"{i:5}", end="")  
        count += 1
        if count % 15 == 0:  
            print()