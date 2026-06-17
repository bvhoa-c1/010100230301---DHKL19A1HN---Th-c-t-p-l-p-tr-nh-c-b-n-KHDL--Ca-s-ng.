def value(x):
    return x + 1  # tính số kế tiếp

# nhập số nguyên từ bàn phím
n = int(input("Nhập một số nguyên: "))

# gọi hàm và in kết quả
count = value(n)
print("Số kế tiếp là:", count)