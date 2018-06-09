age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
money = 10
tot_sum = 0
brother_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        tot_sum += money
        money += 10
        brother_money += 1
    else:
        toy_count += 1

sum = tot_sum + toy_count * toy_price - brother_money

