container = input("Nhập chuỗi container (10 ký tự): ")
bang_ma = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

tong_trong_so = 0
for i in range(10):
    ky_tu = container[i]
    if 'A' <= ky_tu <= 'Z':
        gia_tri = bang_ma[ky_tu]
    else:
        gia_tri = int(ky_tu)
    
    trong_so = gia_tri * (2 ** i)
    tong_trong_so += trong_so

so_kiem_tra = tong_trong_so % 11
if so_kiem_tra == 10:
    so_kiem_tra = 0

print("Số kiểm tra:", so_kiem_tra)