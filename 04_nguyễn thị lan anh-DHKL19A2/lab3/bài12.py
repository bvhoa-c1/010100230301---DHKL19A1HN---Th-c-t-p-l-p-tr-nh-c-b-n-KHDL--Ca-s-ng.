# Bảng mã chữ → số
bang = {
    'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,
    'I':19,'J':20,'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,
    'Q':28,'R':29,'S':30,'T':31,'U':32,'V':34,'W':35,'X':36,
    'Y':37,'Z':38
}

container = input("Nhập mã container (10 ký tự): ").upper()

tong = 0

for i in range(len(container)):
    ky_tu = container[i]
    
    if ky_tu.isalpha():  # nếu là chữ
        gia_tri = bang[ky_tu]
    else:  # nếu là số
        gia_tri = int(ky_tu)
    
    trong_so = gia_tri * (2 ** i)
    tong += trong_so

# tính số kiểm tra
check_digit = tong % 11
if check_digit == 10:
    check_digit = 0

print("Số kiểm tra là:", check_digit)