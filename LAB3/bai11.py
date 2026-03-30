# Bài 11: In ra n số Fibonacci đầu tiên bằng vòng lặp for

def main():
    n = int(input("Nhập n: "))
    if n <= 0:
        print("n phải > 0")
        return
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print(f"{n} số Fibonacci đầu tiên: {' '.join(map(str, fib[:n]))}")

if __name__ == "__main__":
    main()

