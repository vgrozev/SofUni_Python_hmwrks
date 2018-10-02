import pprint

input_key = input()
input_value = input()

num_pairs = int(input())

final_value_list = []
final_dict = {}

pp = pprint.PrettyPrinter(indent=4)

for i in range(0, num_pairs):

    pair = input().split(' => ')
    current_key = pair[0]
    current_value = pair[1].split(';')

    for item in current_value:
        if input_value in item:
            print(item)


pp.pprint(final_dict)