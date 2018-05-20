dist = int(input())
period = input()
price = 0

if dist >= 100:
    price = dist * 0.06
elif 20 <= dist < 100:
    price = dist * 0.09
elif dist < 20 and period == 'day':
    price = dist * 0.79 + 0.70
else:
    price = dist * 0.90 + 0.70

print(price)
