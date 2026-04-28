import msvcrt

def hien_thi_ascii():
    print("Nhập ký tự bất kỳ để xem mã ASCII (Nhấn phím ESC để thoát):")
    
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            
            ma_ascii = ord(char)
            
            if ma_ascii == 27:
                print("\nBạn đã nhấn ESC. Đang thoát chương trình...")
                break
            
            try:
                ky_tu = char.decode('utf-8')
                print(f"Ký tự: {ky_tu} - Mã ASCII: {ma_ascii}")
            except:
                print(f"Ký tự đặc biệt - Mã ASCII: {ma_ascii}")

hien_thi_ascii()