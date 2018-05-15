days_off = int(input())

working_days = 365 - days_off

total_play_time = days_off * 127 + working_days * 63
time_diff = abs(30000 - total_play_time)

hours = time_diff // 60
minutes = time_diff % 60

if total_play_time > 30000:
    output_string = "Tom will run away"
    play_string = 'more'
else:
    output_string = "Tom sleeps well"
    play_string = 'less'

print(output_string)
print("{} hours and {} minutes {} for play".format(hours, minutes, play_string))
