def value(x):
    return x + 1

x = int(input("Nhập số nguyên: "))

count = 1   # có thể đổi nếu đề yêu cầu in nhiều lần

for i in range(count):
    print("Số kế tiếp là:", value(x))