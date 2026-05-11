def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a
print(isAmicable(220, 284))