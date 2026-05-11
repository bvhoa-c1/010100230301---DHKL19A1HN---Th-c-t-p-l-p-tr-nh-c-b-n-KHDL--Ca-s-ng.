n = int(input("Nhập n: "))
original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

if original == reverse:
    print("Là số đối xứng")
else:
    print("Không phải")