# Bài 7.1: Tạo từ điển với khóa x và giá trị x³

N = int(input("Nhập số nguyên N: "))

# Khởi tạo từ điển
my_dict = {x: x**3 for x in range(1, N+1)}

print(f"Từ điển kích thước {N} (khóa: giá trị x³):")
print(my_dict)
