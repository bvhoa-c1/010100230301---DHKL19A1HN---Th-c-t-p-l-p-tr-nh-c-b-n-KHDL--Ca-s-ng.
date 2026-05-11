s = input("Nhập xâu (>10 ký tự): ")
if len(s) > 10:
    print("Từ vị trí 2 đến 8:", s[1:8])
    print("5 ký tự từ vị trí 5:", s[4:9])
    print("3 ký tự cuối:", s[-3:])
    print("Chữ hoa:", s.upper())
    print("Chữ thường:", s.lower())
    print("Đảo ngược:", s[::-1])