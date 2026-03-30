n = int(input("Nhập n: "))
s = str(n)
digits = [int(d) for d in s]

total = sum(digits)
product = 1
for d in digits:
    product *= d
reverse = int(s[::-1])

print(f"Tổng chữ số: {total}")
print(f"Tích chữ số: {product}")
print(f"Số đảo: {reverse}")
