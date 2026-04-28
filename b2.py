def in_fibonacci():
    so_luong = 10 
    a, b = 0, 1  
    
    print(f"Dãy Fibonacci gồm {so_luong} số hạng đầu tiên là: ", end="")
    
    for i in range(so_luong):
        if i == so_luong - 1:
            print(a)
        else:
            print(a, end=", ")
        a, b = b, a + b

print("\n--- Bài 2: In dãy Fibonacci ---")
in_fibonacci()