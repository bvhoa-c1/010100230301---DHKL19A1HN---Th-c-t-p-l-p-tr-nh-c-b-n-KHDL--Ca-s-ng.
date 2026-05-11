inventory = {
    "gold": 550,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"],
    "pocket": ["seashell", "strange berry", "lint"]
}

item = input("item to remove = ")
inventory["backpack"].sort()

if item in inventory["backpack"]:
    inventory["backpack"].remove(item)

print(inventory)
