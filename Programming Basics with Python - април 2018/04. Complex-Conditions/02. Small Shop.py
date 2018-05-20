product = input().lower()
town = input().lower()
quantity = float(input())
total = 0.0

if town == 'sofia':
    if product == 'coffee':
        total = quantity * 0.50
    elif product == 'peanuts':
        total = quantity * 1.60
    elif product == 'beer':
        total = quantity * 1.20
    elif product == 'water':
        total = quantity * 0.80
    else:       # product == 'sweets'
        total = quantity * 1.45
elif town == 'plovdiv':
    if product == 'coffee':
        total = quantity * 0.40
    elif product == 'peanuts':
        total = quantity * 1.50
    elif product == 'beer':
        total = quantity * 1.15
    elif product == 'water':
        total = quantity * 0.70
    else:       # product == 'sweets'
        total = quantity * 1.30
else:   # town == 'Varna'
    if product == 'coffee':
        total = quantity * 0.45
    elif product == 'peanuts':
        total = quantity * 1.55
    elif product == 'beer':
        total = quantity * 1.10
    elif product == 'water':
        total = quantity * 0.70
    else:       # product == 'sweets'
        total = quantity * 1.35

print("{0:.2f}".format(total))
