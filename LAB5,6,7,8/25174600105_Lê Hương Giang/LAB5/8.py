str = input("Nhập chuỗi: ")
if len(str) > 10:
    print("Xâu từ vị trí 2 đến 8:", str[2:9])
    print("Lấy 5 ký tự từ vị trí 5:", str[5:10])
    print("3 ký tự cuối:", str[-3:])
    print("Chữ hoa:", str.upper())
    print("Chữ thường:", str.lower())
    print("Đảo ngược xâu:", str[::-1])
else:
    print("Chuỗi phải lớn hơn 10 ký tự")