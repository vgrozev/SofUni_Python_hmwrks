
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_x = abs(x1 - x2)
side_y = abs(y1 - y2)

area = side_x * side_y
perimeter = 2 * side_x + 2 * side_y

print(area)
print(perimeter)
