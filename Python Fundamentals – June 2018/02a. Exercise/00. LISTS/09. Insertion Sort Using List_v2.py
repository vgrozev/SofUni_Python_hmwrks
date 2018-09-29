input_list = list(map(int, input().split()))

lists_size = len(input_list)
sorted_list = [input_list[0]]  # the first element of the input is automatically the first sorted item
sorted_list_size = len(sorted_list)

for i in range(1, lists_size):

    inserted = False

    for j in range(0, lists_size):

        # if the indexes are equal, that means that the sorted list ran out of elements and a new one has to be inserted
        if j == i or input_list[i] < sorted_list[j]:

            sorted_list.insert(j, input_list[i]) # insert at the index of the larger element
            inserted = True
            break

    # if nothing is inserted during the inner loop, then the item is the biggest one so far, and
    # it is appended at the end of the sorted list
    if not inserted:
        sorted_list.append(input_list[i])

print(*sorted_list)
