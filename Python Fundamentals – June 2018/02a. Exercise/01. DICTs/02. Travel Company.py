data = input()

city_capacity = {}

while data != 'ready':

    list_data = data.split(':')

    city = list_data[0]
    list_transport = list_data[1].split(',')

    if city not in city_capacity:
        city_capacity[city] = {}

    for item in list_transport:
        transport = item.split('-')[0]
        capacity = int(item.split('-')[1])

        city_capacity[city][transport] = capacity

    data = input()

# second loop after the 'ready' keyword

data = input()

while data != 'travel time!':

    city = data.split()[0]
    people = int(data.split()[1])

    total_seats = 0

    for transport_type in city_capacity[city]:

        total_seats += city_capacity[city][transport_type]

    if total_seats >= people:
        print(f"{city} -> all {people} accommodated")
    else:
        print(f'{city} -> all except {people - total_seats} accommodated')

    data = input()
