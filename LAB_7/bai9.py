inventory = {
    "Pen": 20,
    "Book": 10,
    "Bag": 5
}

item = input("Nhap ten mat hang: ")
amount = int(input("Nhap so luong mua: "))

if item in inventory:
    if inventory[item] >= amount:
        inventory[item] -= amount
        print("Giao dich thanh cong")
    else:
        print("Khong du hang")
else:
    print("Khong ton tai mat hang")

print("Ton kho hien tai:")
print(inventory)