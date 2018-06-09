n = int(input())

first_pair = int(input()) + int(input())
previous_pair = first_pair
max_diff = 0

for i in range(1, n):
    temp_pair = int(input()) + int(input())
    temp_diff = abs(previous_pair - temp_pair)
    if temp_diff > max_diff:
        max_diff = temp_diff
    previous_pair = temp_pair

if max_diff == 0:
    print("Yes, value =", first_pair)
else:
    print("No, maxdiff = ", max_diff)
