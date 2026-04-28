def in_day_fibonacci():
    a, b = 0, 1
    count = 0
    max_so_hang = 10
    
    print(f"Dãy Fibonacci ({max_so_hang} số hạng đầu tiên):")
    
    while count < max_so_hang:
        print(a, end=" ")
        tam = a + b
        a = b
        b = tam
        count += 1
    print() 

in_day_fibonacci()