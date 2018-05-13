hour = int(input())
minutes = int(input())

total_min = hour * 60 + minutes + 15

hour = total_min // 60
minutes = total_min % 60

if hour >= 24:
    hour = hour - 24

if minutes < 10:
    print(str(hour) + ":0" + str(minutes))
else:
    print(str(hour) + ":" + str(minutes))


