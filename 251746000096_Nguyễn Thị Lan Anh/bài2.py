# Hàm không có giá trị trả về in ra n số đầu tiên của dãy Fibonacci

def fibonacci():
    n = int(input("Nhập n (n <= 10): "))
    
    a = 0
    b = 1
    
    print("Dãy Fibonacci là:")
    
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Gọi hàm
fibonacci()