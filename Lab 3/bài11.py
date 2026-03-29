n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

a, b = 0, 1  
print("Dãy Fibonacci:", end=" ")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  