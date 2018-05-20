import math

project_hours = int(input())
work_days = int(input())
workers_with_extra_time = int(input())

training_days = work_days * 0.1
actual_work_hours = (work_days - training_days) * 8
extra_hours_worked = workers_with_extra_time * (2 * work_days)
total_work_hours = math.floor(actual_work_hours + extra_hours_worked)

diff_hours = abs(project_hours - total_work_hours)

if total_work_hours >= project_hours:
    print("Yes!{} hours left.".format(diff_hours))
else:
    print("Not enough time!{} hours needed.".format(diff_hours))
