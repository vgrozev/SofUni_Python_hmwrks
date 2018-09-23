data = list(map(int, input().split()))
lookup = int(input())

is_found = False

for item in data:
    if item == lookup:
        is_found = True

if is_found:
    print("yes")
else:
    print("no")
