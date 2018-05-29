test_hour = int(input())
test_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

# calc status
test_total_minutes = test_hour * 60 + test_minutes
arrival_total_minutes = arrival_hour * 60 + arrival_minutes

total_minutes_difference = abs(test_total_minutes - arrival_total_minutes)
hours_difference = total_minutes_difference // 60
minutes_difference = total_minutes_difference % 60


# setting time format
if hours_difference < 1:
    hours_difference = ""
    change = " minutes"
    minutes_difference = str(minutes_difference)
else:
    hours_difference = str(hours_difference)
    change = " hours"
    if minutes_difference < 10:
        minutes_difference = ":0" + str(minutes_difference)
    else:
        minutes_difference = ":" + str(minutes_difference)



# actual calculations
if test_total_minutes - 30 <= arrival_total_minutes <= test_total_minutes:
    arrival = "On Time"
    if test_total_minutes == arrival_total_minutes:
        deviation = ""
    else:
        deviation = " before"
elif test_total_minutes < arrival_total_minutes:
    arrival = "Late"
    deviation = " after"
else:
    arrival = "Early"
    deviation = " before"

#rint part
print(arrival)
if deviation == "":
    print(deviation)
else:
    print(hours_difference + minutes_difference + change + deviation, "the start")
