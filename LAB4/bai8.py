# Bài 8: Tách chữ số n, tổng, tích, số đảo
n = int(input("Nhập n: "))
original = n
s = 0
p = 1
reversed_n = 0
while n > 0:
    digit = n % 10
    s += digit
    p *= digit
    reversed_n = reversed_n * 10 + digit
    n //= 10
print(f"Tổng chữ số: {s}")
print(f"Tích chữ số: {p}")
print(f"Số đảo: {reversed_n}")
