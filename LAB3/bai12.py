letter_values = {
    'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19,
    'J':20, 'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29,
    'S':30, 'T':31, 'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38
}

def letter_to_value(c):
    if c.isdigit():
        return int(c)
    return letter_values.get(c.upper(), 0)

container = input("Nhap ma container 10 ky tu: ").strip()
if len(container) != 10:
    print("Ma phai 10 ky tu!")
else:
    total = 0
    for i in range(10):
        val = letter_to_value(container[i])
        total += val * (1 << i)
    check_digit = total % 11
    if check_digit == 10:
        check_digit = 0
    print(f"Tong: {total}")
    print(f"Check digit: {check_digit}")
    print(f"Ma day du: {container}{check_digit}")
