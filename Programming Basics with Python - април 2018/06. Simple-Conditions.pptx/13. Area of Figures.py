import math

figure = input()

if figure == 'square':
    side = float(input())
    area = pow(side, 2)
elif figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif figure == 'circle':
    radius = float(input())
    area = math.pi * pow(radius, 2)
elif figure == 'triangle':
    base = float(input())
    height = float(input())
    area = base * height / 2

print("{0:.3f}".format(area))
