inventory = {
    'gold' : 732,
    "vat_pham" : ["qua", "dream" , "you"]
}
print(inventory)
# them pocket
inventory["poket"] = ['key of your heart']
# them t8ien neu nhat dc
n = int(input())
inventory["gold"] = inventory["gold"] + n
print("ca[p mhat inventory", inventory)
inventory["backpack"] = ['u', 'my heart', 'gun', 'word', 'ring', 'cf']
inventory['backpack'].sort()
print("xap xep key backpack", inventory['backpack'])
inventory['backpack'].remove("gun")
print("ban con" , inventory["backpack"])