import msvcrt

def in_gia_tri_ascii():
    print("Nhập ký tự bất kỳ để xem mã ASCII (Nhấn phím ESC để thoát):")
    
    while True:
        ky_tu = msvcrt.getch()
        ma_ascii = ord(ky_tu)
        
        if ma_ascii == 27:
            print("\nĐã thoát chương trình.")
            break
            
        print(f"{chr(ma_ascii)}: {ma_ascii}")

in_gia_tri_ascii()