n = int(input())
temp = n
num_digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** num_digits
    temp //= 10

if total == n:
    print("True")
else:
    print("False")