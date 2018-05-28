h = int(input())
x = float(input())
y = float(input())


x1_upper = h
y1_upper = h
x2_upper = 2 * h
y2_upper = 4 * h

x1_lower = 0
y1_lower = 0
x2_lower = 3 * h
y2_lower = h

if ((x1_upper < x < x2_upper) and (y1_upper <= y < y2_upper)) or ((x1_lower < x < x2_lower) and (y1_lower < y < y2_lower)):
    print("Inside")
elif (((x1_upper > x or x > x2_upper) and (y1_upper < y)) or y > y2_upper) or ((x1_lower > x or x > x2_lower) or (y1_lower > y)):
    print("Outside")
else:
    print("Border")
