data = list(map(int, input().split()))

initial_condition = True
swapped = False

while initial_condition or swapped:

    initial_condition = False
    swapped = False

    # Classic version:

    # starts from  the second element and compares it with the previous one
    # for i in range(1, len(data)):
    #     left_element = data[i - 1]
    #     right_element = data[i]
    #
    #     if right_element < left_element:
    #         temp_elem = left_element
    #         data[i - 1] = right_element
    #         data[i] = temp_elem
    #
    #         swapped = True

    # Modern version:

    # starts from  the second element and compares it with the previous one
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            data[i], data[i - 1] = data[i - 1], data[i]
            swapped = True

print(*data)
