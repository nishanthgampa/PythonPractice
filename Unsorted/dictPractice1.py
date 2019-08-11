stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}

def displayInventory(inventory):
	print("Inventory:")
	count = 0
	for k, v in inventory.items():
		print(k + ': ' + str(v))
		count = count + inventory.get(k,0)
	print("Total Number of Items: " + str(count))

#displayInventory(stuff)

def addToInventory(inventory, addeditems):
	for i in addeditems:
		inventory.setdefault(i,0)
		inventory[i] = inventory[i] + 1
	return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
