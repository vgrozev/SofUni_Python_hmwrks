raw_data = input()

inventory = {}

while raw_data != 'shopping time':

    option, product, quantity = raw_data.split(' ')

    if product in inventory:
        inventory[product] = inventory.get(product) + int(quantity)
    else:
        inventory[product] = int(quantity)
    raw_data = input()

raw_data = input()
while raw_data != 'exam time':

    option, product, quantity = raw_data.split(' ')

    if product not in inventory:
        print(f'{product} doesn\'t exist')

    elif product in inventory and inventory.get(product) <= 0:
        print(f'{product} out of stock')

    else:
        inventory[product] = inventory.get(product) - int(quantity)

    raw_data = input()

for key in inventory:
    if inventory[key] > 0:
        print(f'{key} -> {inventory[key]}')
