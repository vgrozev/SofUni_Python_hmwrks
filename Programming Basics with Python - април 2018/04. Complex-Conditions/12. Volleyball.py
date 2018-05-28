import math

year_type = input()
num_holidays = int(input())
num_travel_weekends = int(input())

const_weekends = 48
sofia_weekends = const_weekends - num_travel_weekends
sofia_weekend_games = sofia_weekends * (3.0/4)
holiday_games = (num_holidays) * (2.0/3)
total_games = sofia_weekend_games + num_travel_weekends + holiday_games
leap_year_games = total_games * 0.15

if year_type == 'leap':
    total_games = total_games + leap_year_games

print(math.floor(total_games))


