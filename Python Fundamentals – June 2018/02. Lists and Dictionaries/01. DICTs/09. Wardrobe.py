n = int(input())

clothes_list = []
dict_clothes = {}

for i in range(0, n):
    raw_input = input()
    data = raw_input.split(' -> ')
    color = data[0]
    clothes_list = data[1].split(',')

    if color not in dict_clothes:
        dict_clothes[color] = {}

    for item in clothes_list:
        if item in dict_clothes[color]:
            dict_clothes[color][item] = dict_clothes[color].get(item) + 1
        else:
            dict_clothes[color][item] = 1

lookup_item = input().split()
for key in dict_clothes:
    print(f'{key} clothes:')
    for val in dict_clothes[key]:
        if lookup_item[0] == key and lookup_item[1] == val:
            print(f'* {val} - {dict_clothes[key][val]} (found!)')
        else:
            print(f'* {val} - {dict_clothes[key][val]}')