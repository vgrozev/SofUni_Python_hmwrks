import math

area_X = int(input())
grape_per_sq_m_Y = float(input())
liters_needed_Z = int(input())
workers = int(input())

total_grape = area_X * grape_per_sq_m_Y
total_wine = (total_grape * 0.4) / 2.5
wine_diff = abs(total_wine - liters_needed_Z)
wine_per_worker = math.ceil(wine_diff / workers)

if total_wine >= liters_needed_Z:
    print("Good harvest this year! Total wine: {} liters.".format(math.floor(total_wine)))
    print("{} liters left -> {} liters per person.".format(math.ceil(wine_diff), wine_per_worker))
else:
    print("It will be a tough winter! More {} liters wine needed.".format(math.floor(wine_diff)))




