ints = list(map(int, input().split(" ")))

no_negative_list = []

for item in reversed(ints):
    if item >= 0:
        no_negative_list.append(item)

if no_negative_list:
    for i in no_negative_list:
        print(i, end=" ")
else:
    print("empty")

