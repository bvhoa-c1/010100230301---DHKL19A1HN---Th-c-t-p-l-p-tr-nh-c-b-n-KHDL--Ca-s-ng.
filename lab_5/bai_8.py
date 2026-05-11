s = input("s = ")

if len(s) <= 10:
    print("Length must be greater than 10")
else:
    print(s[1:8])
    print(s[4:9])
    print(s[-3:])
    print(s.upper())
    print(s.lower())
    print(s[::-1])
