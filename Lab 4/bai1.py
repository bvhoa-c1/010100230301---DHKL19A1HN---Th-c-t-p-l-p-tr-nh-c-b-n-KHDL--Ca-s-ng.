n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

a, b = 0, 1   
count = 1     

while count < n:
    a, b = b, a + b
    count += 1

print(f"Số Fibonacci thứ {n} là:", a)