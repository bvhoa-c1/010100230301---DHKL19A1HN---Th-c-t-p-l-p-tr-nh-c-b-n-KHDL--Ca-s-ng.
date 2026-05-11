# Xử lý chuỗi theo yêu cầu bài 5.8

s = input("Nhập chuỗi: ")

if len(s) <= 10:
    print("Chuỗi phải có độ dài lớn hơn 10 ký tự.")
else:

    # Từ vị trí 2 đến 8
    sub1 = s[1:8]

    # 5 ký tự từ vị trí 5
    sub2 = s[4:9]

    # 3 ký tự cuối
    last3 = s[-3:]

    # Chuyển thành chữ hoa
    upper_s = s.upper()

    # Chuyển thành chữ thường
    lower_s = s.lower()

    # Đảo ngược chuỗi
    reverse_s = s[::-1]

    # Hiển thị kết quả
    print("Xâu từ vị trí 2 đến 8:", sub1)
    print("5 ký tự từ vị trí 5:", sub2)
    print("3 ký tự cuối:", last3)
    print("Chữ hoa:", upper_s)
    print("Chữ thường:", lower_s)
    print("Xâu đảo ngược:", reverse_s)