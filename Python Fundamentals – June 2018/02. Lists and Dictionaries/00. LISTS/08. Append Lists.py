input_lists = list(input().split('|'))


result_list = []

for item in reversed(input_lists):
    temp_list = item.split(" ")
    for i in temp_list:
        if i != "":
            result_list.append(i)

print(*result_list, sep=" ")
