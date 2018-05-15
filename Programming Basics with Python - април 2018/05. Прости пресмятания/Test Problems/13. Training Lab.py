
w = float(input())
h = float(input())

work_place_width_in_cm = 120
work_place_height_in_cm = 70
corridor_in_cm = 100
number_of_missing_desks = 3

# convert width and height to centimeters
w_to_cm = w * 100
h_to_cm = h * 100

# find the total number of rows (integer division)
number_of_rows = w_to_cm // work_place_width_in_cm

# subtract the corridor from the total height
h_to_cm = h_to_cm - 100

# find the number of desks in one row, excluding the corridor (integer division)
desks_in_a_row = h_to_cm // 70

# find the total number of desks if there is no door and teacher area
all_desks = number_of_rows * desks_in_a_row - number_of_missing_desks


print(all_desks)





