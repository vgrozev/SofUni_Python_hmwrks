data = list(map(int, input().split()))

sorted_list = sorted(data)
list_size = len(sorted_list)
current_num = 0

if list_size == 1:
    print("{0} -> {1}".format(sorted_list[0], 1))

else:
    for i in range(0, list_size - 1):
        current_num = sorted_list[i]
        if sorted_list[i] != sorted_list[i + 1] or i == list_size - 2: # to handle the case where the last few are the same
            print("{0} -> {1}".format(sorted_list[i], sorted_list.count(current_num)))

    if sorted_list[-1] != sorted_list[-2]:  # handles the case where the last element is a new number not matching others
        print("{0} -> {1}".format(sorted_list[-1], 1))
