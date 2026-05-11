s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
tim_thay = False
for ch in s1:
    if ch in s2:
        print("Chuỗi con chung ngắn nhất là:", ch)
        tim_thay = True 
        break
if not tim_thay:
    print("Không có chuỗi chung nào")