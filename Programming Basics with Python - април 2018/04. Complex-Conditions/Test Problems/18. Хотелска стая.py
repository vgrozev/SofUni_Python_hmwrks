month = input()
num_nights = int(input())

discount = 0
studio = 0
apartment = 0

if month == "May" or month == "October":
    apartment = num_nights * 65
    studio = num_nights * 50
    if 7 < num_nights < 14:
        discount = studio * 0.05
    elif num_nights > 14:
        discount = studio * 0.3
elif month == "June" or month == "September":
    apartment = num_nights * 68.70
    studio = num_nights * 75.20
    if num_nights > 14:
        discount = studio * 0.2
elif month == "July" or month == "August":
    apartment = num_nights * 77
    studio = num_nights * 76

studio = studio - discount

if num_nights > 14:
    apartment = apartment - (apartment * 0.1)

print("Apartment: {:.2f} lv.".format(apartment))
print("Studio: {:.2f} lv.".format(studio))
