s = input("Nhap chuoi: ")

num_str = ""

for ch in s:
    if ch.isdigit():
        num_str += ch

if num_str == "":
    print("Khong co chu so")
else:
    num = int(num_str)
    print("So sau khi tach:", num)

    # Kiem tra nguyen to
    prime = True

    if num < 2:
        prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break

    if prime:
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")