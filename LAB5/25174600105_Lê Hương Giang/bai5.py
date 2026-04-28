import msvcrt

def ASCII():
    print("Nhấn phím bất kì để xem giá trị ASCII, nhấn ESC để kết thúc")
    while True:
        c = msvcrt.getch()
        if ord(c) == 27:
            break
        print(f"Giá trị ASCII của ký tự '{c.decode()}' là {ord(c)}")

ASCII()