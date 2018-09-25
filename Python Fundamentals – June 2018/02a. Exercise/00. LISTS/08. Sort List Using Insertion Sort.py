data = list(map(int, input().split()))

initial_condition = True
swapped = False

for i in range(1, len(data)):

    # starts assuming that the first element is the smallest and already sorted.
    # then continues to compare the next element with the one before
    # If it finds smaller it flips it with the previous and goes on until it finds the correct place backwards
    while data[i] < data[i - 1] and i > 0:
        data[i], data[i - 1] = data[i - 1], data[i]
        i -= 1
        #print(data)

print(*data)
