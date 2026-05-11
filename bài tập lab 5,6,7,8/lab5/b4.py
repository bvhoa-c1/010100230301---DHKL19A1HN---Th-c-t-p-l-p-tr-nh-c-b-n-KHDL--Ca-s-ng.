s = input("Nhập xâu: ")
digits = ""
for ch in s:
    if ch.isdigit():
        digits += ch
if digits == "":
    print("Không có chữ số nào")
else:
    num = int(digits)
    if num < 2:
        print(num, "không là số nguyên tố")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "là số nguyên tố")
        else:
            print(num, "không là số nguyên tố")