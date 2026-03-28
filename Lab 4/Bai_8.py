n = int(input())
temp = n
sum_digits = 0
prod_digits = 1 if n > 0 else 0
rev_num = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    prod_digits *= digit
    rev_num = rev_num * 10 + digit
    temp //= 10

print(sum_digits)
print(prod_digits)
print(rev_num)