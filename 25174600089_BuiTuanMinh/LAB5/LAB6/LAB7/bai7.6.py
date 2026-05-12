inventory = {
    "gold": 50,
    "sword":2,
    "potion":10,
    "shield":3,
}
print("inventory ban đầu:")
for k, v in inventory.items():
    print(k,v)
nhap = input("\nNhập các vật phẩm trong pocket (cách nhau dấu phẩy): ")
inventory["pocket"] = [item.strip() for item in nhap.split(",")]

them_gold = int(input("Nhập số gold cần thêm: "))
inventory["gold"] += them_gold

print("\nInventory sau khi cập nhật:")
for k, v in inventory.items():
    print(f"  {k}: {v}")