def tim_so(n):
    res = n
    
    p = 1
    while True:
        
        tmp = (n // p - 1) * p + (p - 1)
        
        if tmp < 0:
            break
      
        def tong(x): return sum(int(d) for d in str(x))
        
        if tong(tmp) >= tong(res):
            res = tmp
            
        p *= 10 
        if p > n:
            break
            
    return res

n = int(input("Nhập n: "))
print("Số có tổng chữ số lớn nhất là:", tim_so(n))
