# Từ điển inventory ban đầu
inventory = {
    "gold": 500,
    "rope": 1,
    "torch": 6,
    "arrow": 12
}

# Hiển thị inventory ban đầu
print("Inventory ban đầu:")
print(inventory)

# Thêm khóa 'pocket' chứa danh sách vật phẩm
inventory["pocket"] = ["key", "knife", "coin"]

# Cập nhật số lượng gold
inventory["gold"] += 100

# Hiển thị inventory sau khi cập nhật
print("\nInventory sau khi cập nhật:")
for key, value in inventory.items():
    print(key, ":", value)