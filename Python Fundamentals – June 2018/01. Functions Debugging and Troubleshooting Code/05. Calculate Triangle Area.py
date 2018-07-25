base = float(input())
height = float(input())


def triangle_area(b, h):
    area = (b * h) / 2

    return area


result = triangle_area(base, height)
print(f"{result:.12g}")
