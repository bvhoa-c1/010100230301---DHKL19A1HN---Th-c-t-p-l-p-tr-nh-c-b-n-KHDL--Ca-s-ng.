bang_ma_hoa = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

# Nhập mã container (dùng upper() để đề phòng người dùng nhập chữ thường)
ma_container = input("Nhập chuỗi 10 ký tự mã container: ").upper()

# Kiểm tra xem người dùng có nhập đúng 10 ký tự không
if len(ma_container) != 10:
    print("Lỗi: Mã container phải có đúng 10 ký tự!")
else:
    tong_trong_so = 0
    
    # Bước 1 & 2: Dùng vòng lặp for chạy từ vị trí 0 đến 9
    for i in range(0,10):
        ky_tu = ma_container[i]
        
        # Nếu ký tự là chữ cái (trong 4 ký tự đầu)
        if ky_tu.isalpha():
            gia_tri = bang_ma_hoa[ky_tu]
        # Nếu ký tự là số (giữ nguyên giá trị)
        else:
            gia_tri = int(ky_tu)
            
        # Tính trọng số: giá trị * 2^i
        trong_so = gia_tri * (2 ** i)
        
        # In ra từng bước tính toán để đối chiếu với ví dụ của đề bài
        print(f"w{i} = {gia_tri} x 2^{i} = {trong_so}")
        
        # Cộng dồn vào tổng
        tong_trong_so += trong_so
        
    # Bước 3: Tính số kiểm tra
    print(f"\nTổng các trọng số: {tong_trong_so}")
    
    so_kiem_tra = tong_trong_so % 11
    
    # Xử lý trường hợp ngoại lệ: nếu số dư là 10 thì số kiểm tra là 0
    if so_kiem_tra == 10:
        so_kiem_tra = 0
        
    print(f"Số kiểm tra = {tong_trong_so} : 11 dư {so_kiem_tra}")
    print(f"Vậy số kiểm tra của mã container {ma_container} là {so_kiem_tra}.")