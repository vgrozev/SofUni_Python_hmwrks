list_numbers = list(map(int, input().split(' ')))


for index in range(0, len(list_numbers)):
    if index % 2 != 0 and list_numbers[index] % 2 != 0:
        print(f"Index {index} -> {list_numbers[index]}")
