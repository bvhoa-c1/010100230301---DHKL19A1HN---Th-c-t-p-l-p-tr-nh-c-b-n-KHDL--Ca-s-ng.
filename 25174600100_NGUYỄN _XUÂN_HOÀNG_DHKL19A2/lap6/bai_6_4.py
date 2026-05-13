# Bài 6.4: Tạo danh sách Fibonacci sử dụng List Comprehension

n = int(input("Nhập số hạng đầu tiên của dãy Fibonacci: "))

# Tạo dãy Fibonacci
fibonacci = []
a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

# Cách khác sử dụng List Comprehension (yêu cầu hàm phụ)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_lc = [f for f in fib(n)]

print(f"Dãy Fibonacci {n} số hạng đầu tiên: {fibonacci}")
print(f"Sử dụng List Comprehension: {fibonacci_lc}")
