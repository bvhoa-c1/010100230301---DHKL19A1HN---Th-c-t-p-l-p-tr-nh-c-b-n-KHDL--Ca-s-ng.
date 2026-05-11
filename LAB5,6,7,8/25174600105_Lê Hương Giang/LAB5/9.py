s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

if s1 == s2:
    print("Hai chuỗi giống nhau")

else:

    if len(s1) < len(s2):
        print("Có thể thêm ký tự để chuyển đổi")

    elif len(s1) > len(s2):
        print("Có thể xóa ký tự để chuyển đổi")

    else:
        print("Có thể thay thế ký tự để chuyển đổi")