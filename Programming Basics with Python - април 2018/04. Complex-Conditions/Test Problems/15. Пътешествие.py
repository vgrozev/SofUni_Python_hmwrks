budget = float(input())
season = input().lower()

if budget <= 100:
    destination = "Somewhere in Bulgaria"
    if season == "summer":
        accommodation = "Camp -"
        spent = budget * 0.3
    else:
        accommodation = "Hotel -"
        spent = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Somewhere in Balkans"
    if season == "summer":
        accommodation = "Camp -"
        spent = budget * 0.4
    else:
        accommodation = "Hotel -"
        spent = budget * 0.8
else:
    destination = "Somewhere in Europe"
    accommodation = "Hotel -"
    spent = budget * 0.9

print(destination)
print(accommodation, "{0:.2f}".format(spent))

