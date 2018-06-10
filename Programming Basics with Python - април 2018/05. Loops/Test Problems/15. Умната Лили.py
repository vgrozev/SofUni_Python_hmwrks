age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
money = 10
money_sum = 0
brother_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money_sum += money
        money += 10
        brother_money += 1
    else:
        toy_count += 1

tot_sum = money_sum + toy_count * toy_price - brother_money
diff = abs(tot_sum - washer_price)

if tot_sum < washer_price:
    message = 'No! {:.2f}'.format(diff)
else:
    message = 'Yes! {:.2f}'.format(diff)

print(message)
