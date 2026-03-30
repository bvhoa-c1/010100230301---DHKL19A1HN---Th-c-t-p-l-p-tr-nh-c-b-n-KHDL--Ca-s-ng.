gia_tri_ky_tu = {
    'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20,
    'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31,
    'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38
}

container = input("Nhập mã container 10 ký tự: ").upper()
n = len(container)

tong = 0
for i in range(n):
    c = container[i]
    if i < 4:
        val = gia_tri_ky_tu[c]
    else:
        val = int(c)
    tong += val * (2 ** i)

check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("Số kiểm tra container là:", check_digit)