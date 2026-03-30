# Bài 12: Tính số kiểm tra container (check digit) sử dụng vòng lặp for

# Bảng mã hóa chữ cái (bỏ bội 11)
chu_cai = {
    'A':10, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20,
    'K':21, 'L':23, 'M':24, 'N':25, 'O':26, 'P':27, 'Q':28, 'R':29, 'S':30, 'T':31,
    'U':32, 'V':34, 'W':35, 'X':36, 'Y':37, 'Z':38
}

def gia_tri_ky_tu(c):
    if c.isdigit():
        return int(c)
    else:
        return chu_cai.get(c.upper(), 0)

def main():
    container = input("Nhập mã container 10 ký tự: ").strip()
    if len(container) != 10:
        print("Phải là 10 ký tự!")
        return
    
    tong = 0
    for i in range(10):
        giatri = gia_tri_ky_tu(container[i])
        trong_so = giatri * (2 ** i)
        tong += trong_so
        print(f"w{i} = {giatri} * 2^{i} = {trong_so}")
    
    du = tong % 11
    if du == 10:
        du = 0
    print(f"Tổng trọng số: {tong}")
    print(f"Số kiểm tra (tổng % 11): {du}")

if __name__ == "__main__":
    main()

