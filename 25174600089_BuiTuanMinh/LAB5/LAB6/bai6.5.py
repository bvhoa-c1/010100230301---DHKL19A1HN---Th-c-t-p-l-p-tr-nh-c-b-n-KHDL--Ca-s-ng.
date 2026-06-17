def so_nguyen_to(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
nguyen_to = [x for x in range(2,100)if so_nguyen_to(x)]
print(nguyen_to)
print(len(nguyen_to))
