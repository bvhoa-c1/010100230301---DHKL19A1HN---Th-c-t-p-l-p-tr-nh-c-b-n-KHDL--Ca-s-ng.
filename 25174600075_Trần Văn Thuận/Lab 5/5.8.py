chuoi = input("Nhập chuỗi có độ dài > 10 ký tự: ")
if len(chuoi) <= 10:
    print("Lỗi: chuỗi không lớn hơn 10")
else:
    print("1. Từ vị trí 2 đến 8:", chuoi[2:9])
    print("2. 5 ký tự từ vị trí 5:", chuoi[4:9])
    print("3. 3 ký tự cuối:", chuoi[-3:])
    print("4. Viết hoa:", chuoi.upper())
    print("5. Viết thường.", chuoi.lower())
    print("5. Đảo ngược chuỗi:", chuoi[::-1])
