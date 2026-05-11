n = int(input("Nhập n: "))
fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2])for i in range(n-1)]
print(f"{n} số Fibonacci đầu tiên là: {fibonacci[:n]}")
