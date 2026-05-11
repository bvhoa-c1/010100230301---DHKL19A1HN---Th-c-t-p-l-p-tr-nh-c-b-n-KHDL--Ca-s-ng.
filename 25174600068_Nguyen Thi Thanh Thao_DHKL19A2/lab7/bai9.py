ton_kho = {
    "but": 10,
    "sua": 5,
    "banh": 8
}

da_ban = {
    "but": 2,
    "banh": 3
}

for mat_hang in da_ban:
    if mat_hang in ton_kho:
        ton_kho[mat_hang] -= da_ban[mat_hang]

print("Ton kho sau giao dich:")
print(ton_kho)