n = int(input("Nhập n: "))

S2 = 0
a = 1

while a<=n:
    S2 = 1/(3 ** (2 * a + 1))
    a += 1

print(f"S1 = {S2}")