# Hàm nhập ký tự và in mã ASCII, dừng khi nhấn ESC

import msvcrt

def ascii_ky_tu():
    print("Nhấn phím bất kỳ để xem mã ASCII")
    print("Nhấn ESC để thoát")

    while True:
        ky_tu = msvcrt.getch()   # đọc 1 phím
        
        if ky_tu == b'\x1b':     # phím ESC
            print("Kết thúc chương trình")
            break
        
        print("Ký tự:", ky_tu.decode('utf-8'), "- ASCII:", ord(ky_tu))

# Gọi hàm
ascii_ky_tu()