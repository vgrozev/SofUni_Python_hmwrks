town = input().capitalize()
s = float(input())

fee = 0

if town == "Sofia":
    if 0 <= s <= 500:
        fee = s * 0.05
    elif 500 < s <= 1000:
        fee = s * 0.07
    elif 1000 < s <= 10000:
        fee = s * 0.08
    elif s > 10000:
        fee = s * 0.12
    else:
        fee = "error"
elif town == "Varna":
    if 0 <= s <= 500:
        fee = s * 0.045
    elif 500 < s <= 1000:
        fee = s * 0.075
    elif 1000 < s <= 10000:
        fee = s * 0.1
    elif s > 10000:
        fee = s * 0.13
    else:
        fee = "error"
elif town == "Plovdiv":
    if 0 <= s <= 500:
        fee = s * 0.055
    elif 500 < s <= 1000:
        fee = s * 0.08
    elif 1000 < s <= 10000:
        fee = s * 0.12
    elif s > 10000:
        fee = s * 0.145
    else:
        fee = "error"
else:
    fee = "error"

if fee == "error":
    print(fee)
else:
    print("{:.2f}".format(fee))