input_list = list(map(int, input().split()))

# working dummy solution:

lists_size = len(input_list)
sorted_list = [None] * lists_size  # put 'None' as a placeholder to guarantee that indexes exist.

for i in range(0, lists_size):

    inserted = False
    # if the sorted lis is empty, or
    # if item with the same index from input is smaller then the item at that index in the sorted list,
    # insert the first one at the index of the second one
    for j in range(0, lists_size):
        if sorted_list[j] is None or input_list[i] < sorted_list[j]:

            sorted_list.insert(j, input_list[i])
            inserted = True
            break

    # if nothing is inserted during the inner loop, then the item is the biggest one so far, and
    # it is appended at the end of the sorted least
    if not inserted:
        sorted_list.append(input_list[i])

# remove all of the placeholders
while None in sorted_list:
        sorted_list.remove(None)

print(*sorted_list)

