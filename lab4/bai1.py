# Nhập vị trí n cần tìm
n = int(input("Nhập n: "))

# Khởi tạo các giá trị ban đầu
a = 0 
b = 1  
count = 0  # Biến đếm vị trí hiện tại


if n <= 0:
    fib_n = 0
else:
    
    while count < n:
        
        a, b = b, a + b
        count += 1
        fib_n = a
        print(fib_n,end=" ")
print()
print(f"Số Fibonacci thứ {n} là: {fib_n}")