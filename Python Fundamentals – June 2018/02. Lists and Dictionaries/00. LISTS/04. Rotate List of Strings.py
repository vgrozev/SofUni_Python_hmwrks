list_strings = input().split(' ')

last = list_strings.pop()

list_strings.insert(0, last)

for item in list_strings:
    print(item, end=' ')






