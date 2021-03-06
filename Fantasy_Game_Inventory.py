stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " +str(item_total))

def addToInventory(inventory, addedItems):
    for elements in addedItems:
        if elements in inventory.keys():
            inventory[elements] = inventory.get(elements) + 1
        else:
            inventory.setdefault(elements,1)
    return inventory

display_inventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)
