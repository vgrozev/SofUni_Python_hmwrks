data = list(map(int, input().split()))
input_number = int(input())

for i in range(1, len(data)):

    # The same as problem # 08, but in reverse. '>' in the while loop, instead of '<'
    # "while data[i] < data[i - 1] and i > 0:"  ---> original line
    while data[i] > data[i - 1] and i > 0:
        data[i], data[i - 1] = data[i - 1], data[i]
        i -= 1

# print the first N items (input_number)
for item in range(0, input_number):
    print(data[item], end=' ')
