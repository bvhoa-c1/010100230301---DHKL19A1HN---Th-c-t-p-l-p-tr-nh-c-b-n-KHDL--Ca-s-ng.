def in_fibonaci(n):
    fib1=0
    fib2=1
    i=0
    while i<n:
        print(fib1)
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        i+=1
print("10 so dau tien")
in_fibonaci(10)