kho = {
    "Táo": 20,
    "cam": 15,
    "Bánh": 23
}
ban_ra = {
    "Táo": 5,
    "Bánh": 10
}
for hang in ban_ra:
    if hang in kho:
        kho[hang] -= ban_ra[hang]
print("tồn kho sau cập nhật:")
for hang in kho:
    print(hang, ":", kho[hang])