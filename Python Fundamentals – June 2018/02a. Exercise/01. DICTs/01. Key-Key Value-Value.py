input_key = input().strip()
input_value = input().strip()

num_pairs = int(input())

final_dict = {}

for i in range(0, num_pairs):

    pair = input().split(' => ')
    current_key = pair[0]
    current_value = pair[1].split(';')

    # if the input_key is at least a substring of the currently processed key,
    # loop trough the current_value list.
    # if the input_value is contained in any of the items of the current_value list,
    # add those items to a list which is a value for the current key.
    # Add the current_key and this list of values as a key-value pair to the final_dict
    if input_key in current_key:

        if current_key not in final_dict:
            final_dict[current_key] = []

        for item in current_value:
            if input_value in item:
                item.strip()
                final_dict[current_key].append(item)

for key in final_dict:
    print(f'{key}:')
    for value in final_dict[key]:
        print(f'-{value}')
