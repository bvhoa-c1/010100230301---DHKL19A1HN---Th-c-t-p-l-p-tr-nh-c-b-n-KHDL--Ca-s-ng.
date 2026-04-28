def in_day_fibonacci():
    n1, n2 = 0, 1
    count = 0
    so_luong = 10
    
    print(f"Dãy {so_luong} số Fibonacci đầu tiên là:")
    while count < so_luong:
        print(n1, end=" ")
        # Tính toán số tiếp theo
        tiep_theo = n1 + n2
        # Cập nhật lại giá trị
        n1 = n2
        n2 = tiep_theo
        count += 1
    print() 
in_day_fibonacci()