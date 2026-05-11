# Quản lý inventory

inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

# Thêm khóa pocket
inventory["pocket"] = ["seashell", "strange berry", "lint"]

# Cập nhật gold
inventory["gold"] += 50

print(inventory)