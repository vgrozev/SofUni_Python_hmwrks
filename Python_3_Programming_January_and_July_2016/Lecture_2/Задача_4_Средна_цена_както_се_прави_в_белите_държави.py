
price_list = []
current_price = ''

while current_price != 'stop' :
    current_price = input("Enter a price (or 'stop'): ")
    if current_price == 'stop':
        print("All prices: ")
        print(price_list)
    else:
        price_list.append(float(current_price))

#price_list = [23.0, 23.0, 23.0, 34.0,234453.0, 32.0, 2323.0, 435.0, 23.0, 53.0, 23.0, 345.0, 234453.0]
#price_list = [1.0, 10.0, 7.34, 12.75, 22.5]
print(price_list)
max_price = max(price_list)
min_price = min(price_list)
print("max price = " + str(max_price))
print("min price = " + str(min_price))
print("")

while min_price in price_list:
    price_list.remove(min_price)
while max_price in price_list:
    price_list.remove(max_price)

if len(price_list) < 2:
    print("The list is not full: ")
else:
    print("The price list with min and max remived is: "),
    print(price_list)

    print("The size of the list is: "),
    print(len(price_list))

    print("Average price is"),
    print(sum(price_list)/len(price_list))
