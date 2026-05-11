
s = input("Nhap chuoi: ")

digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

print("Chuoi chi gom chu so:", digits)

if digits == "":
    print("Khong co chu so nao!")
else:
    number = int(digits)

    # Kiem tra so nguyen to
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(number, "la so nguyen to")
    else:
        print(number, "khong la so nguyen to")