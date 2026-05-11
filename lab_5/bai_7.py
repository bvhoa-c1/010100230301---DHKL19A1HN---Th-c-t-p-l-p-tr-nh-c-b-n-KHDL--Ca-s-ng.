s = input("s = ")

lower = sum(1 for ch in s if ch.islower())
upper = sum(1 for ch in s if ch.isupper())
digit = sum(1 for ch in s if ch.isdigit())
special = sum(1 for ch in s if not ch.isalnum())

print("lower =", lower)
print("upper =", upper)
print("digit =", digit)
print("special =", special)
