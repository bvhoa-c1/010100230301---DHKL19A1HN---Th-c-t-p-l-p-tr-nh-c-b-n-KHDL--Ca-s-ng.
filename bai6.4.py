# Tạo danh sách Fibonacci bằng List Comprehension

n = int(input("Nhập số lượng số Fibonacci: "))

fibo = [0, 1]

# Sinh thêm các phần tử Fibonacci
[fibo.append(fibo[i - 1] + fibo[i - 2]) for i in range(2, n)]

# Xử lý trường hợp đặc biệt
if n == 1:
    fibo = [0]
elif n == 0:
    fibo = []

print("Dãy Fibonacci:")
print(fibo)