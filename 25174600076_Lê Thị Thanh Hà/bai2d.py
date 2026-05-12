def tim_min(a, b, c):
    return min(a, b, c)

def tim_max(a, b, c):
    return max(a, b, c)

# Test
a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))

print("Số nhỏ nhất:", tim_min(a, b, c))
print("Số lớn nhất:", tim_max(a, b, c))