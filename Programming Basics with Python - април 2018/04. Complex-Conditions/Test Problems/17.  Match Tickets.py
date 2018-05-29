budget = float(input())
category = input()
num_people = int(input())


if category == "VIP":
    cost = 499.99
else:
    cost = 249.99


if category == "VIP":
    if 1 <= num_people <= 4:
        transport = budget * 0.75
    elif 5 <= num_people <= 9:
        transport = budget * 0.60
    elif 10 <= num_people <= 24:
        transport = budget * 0.5
    elif 25 <= num_people <= 49:
        transport = budget * 0.4
    else:
        transport = budget * 0.25
else:
    if 1 <= num_people <= 4:
        transport = budget * 0.75
    elif 5 <= num_people <= 9:
        transport = budget * 0.60
    elif 10 <= num_people <= 24:
        transport = budget * 0.5
    elif 25 <= num_people <= 49:
        transport = budget * 0.4
    else:
        transport = budget * 0.25

total_cost = cost * num_people
actual_money = budget - transport

if total_cost < actual_money:
    message = "Yes! You have {:.2f} leva left.".format(actual_money - total_cost)
else:
    message = "Not enough money! You need {:.2f} leva.".format(total_cost - actual_money)

print(message)
