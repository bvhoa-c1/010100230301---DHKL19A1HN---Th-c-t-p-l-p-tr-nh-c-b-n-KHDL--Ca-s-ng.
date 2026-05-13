# Windows: chạy trên Windows console
import msvcrt

def ascii_loop():
    """Đọc ký tự không cần Enter, in mã ASCII, dừng khi nhấn ESC."""
    print("Nhấn phím (ESC để thoát).")
    while True:
        ch = msvcrt.getch()  # trả về bytes
        # Một số phím trả về b'\x00' hoặc b'\xe0' trước mã phím mở rộng
        if ch in (b'\x00', b'\xe0'):
            # đọc tiếp mã mở rộng và hiển thị thông tin dạng mở rộng
            ext = msvcrt.getch()
            print(f"Phím mở rộng, mã bytes: {ch + ext}  (hiển thị không in được ASCII)")
            continue
        code = ch[0]
        if code == 27:  # ESC
            print("Đã nhấn ESC. Kết thúc.")
            break
        # In ký tự nếu có thể hiển thị, kèm mã ASCII
        try:
            char = ch.decode('utf-8')
        except UnicodeDecodeError:
            char = '?'
        print(f"Ký tự: {char!r}  ASCII: {code}")

if __name__ == "__main__":
    ascii_loop()
