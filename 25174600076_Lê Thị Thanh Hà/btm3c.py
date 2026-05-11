

def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]

dem = 0

for i in range(1, 1001):
    if la_so_doi_xung(i):
        print(f"{i:5}", end="")
        dem += 1
        
        if dem % 15 == 0:
            print()