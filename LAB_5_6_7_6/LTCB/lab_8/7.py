m , n = map(int, (input().split()))
if m == n:
    print("k hop le dk thuat toan")
    exit()
def  Amicable(m , n):
    sum1 = sum2 = 0
    hi = n
    hu = m
    for i in range(1, m):
        if m % i == 0:
            sum1 += i
    for j in range(1, n):
        if n % j == 0:
            sum2 += j
    if sum1 == hi and sum2 == hu:
        print("la cap so Amicable")
    else:
        print("k la  Amicable")
    return sum1 , sum2
print(Amicable(m , n))



