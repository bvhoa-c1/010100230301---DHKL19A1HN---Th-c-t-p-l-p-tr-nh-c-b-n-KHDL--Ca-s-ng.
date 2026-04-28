import msvcrt
def in_ascii():
    print("chương trình mã ASCII")
    print("Nhấn phím bất kì để xem mã ASCII. Nhấn phím 'ESC' để thoát")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            ma_ascii = ord(char)
            if ma_ascii == 27:
                print("\n Bạn đã nhấn ESC. Đang thoát chương trình")
                break
            try:
                ky_tu = char.decode('utf-8')
                print(f"Ký tự: {ky_tu}-> Mã ASCII:{ma_ascii}")
            except:
                print(f"Kỹ tự đặc biệt -> Mã ASCII: {ma_ascii}")
in_ascii()