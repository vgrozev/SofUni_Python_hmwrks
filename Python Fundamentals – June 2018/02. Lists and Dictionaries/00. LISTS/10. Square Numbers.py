import math

ints = list(map(int, input().split(" ")))
sqrt_list = []

for item in ints:
    if item > 0 and math.sqrt(item) == int(math.sqrt(item)):
        sqrt_list.append(item)

sqrt_list.sort(reverse=True)

print(*sqrt_list, end=" ")

