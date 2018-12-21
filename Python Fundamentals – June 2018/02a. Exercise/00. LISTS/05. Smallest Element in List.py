data = list(map(int, input().split()))

smallestInt = data[0]

for element in data:
    if element < smallestInt:
        smallestInt = element
print(smallestInt)

