# Bài 12: Tính số kiểm tra container (check digit)

# Bảng mã hóa chữ cái (bỏ bội 11)
letter_values = {'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20, 
                 'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31, 
                 'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38}

container = input("Nhập mã container 10 ký tự: ").upper().strip()

if len(container) != 10:
    print("Mã phải 10 ký tự!")
else:
    total = 0
    for pos in range(10):
        ch = container[pos]
        if ch.isdigit():
            val = int(ch)
        elif ch.isalpha():
            val = letter_values.get(ch, 0)
        else:
            print("Ký tự không hợp lệ!")
            break
        weight = val * (2 ** pos)
        total += weight
    else:
        check_digit = total % 11
        if check_digit == 10:
            check_digit = 0
        print(f"Số kiểm tra: {check_digit}")

# Test ví dụ SUDU307007

