s1 = input("Nhập chuỗi ban đầu: ")
s2 = input("Nhập chuỗi mục tiêu: ")

if sorted(s1) == sorted(s2):
    print("Có thể chuyển đổi")
else:
    print("Không thể chuyển đổi")
