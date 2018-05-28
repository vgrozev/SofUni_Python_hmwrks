num = int(input())

week_days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


if 0 <= num < len(week_days):
    print(week_days[num])
else:
    print("Error")