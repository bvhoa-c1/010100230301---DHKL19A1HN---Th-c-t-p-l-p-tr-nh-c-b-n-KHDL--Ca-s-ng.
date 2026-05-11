s = input("Nhap chuoi: ")

number = ""

for ch in s:
    if ch.isdigit():
        number += ch

print("So sau khi loc:", number)

n = int(number)
prime = True
if n < 2:
    prime = False

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

if prime:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")