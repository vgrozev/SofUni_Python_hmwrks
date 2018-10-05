n = int(input())
l = int(input())

first_small = 97
upper_limit = n + 1

for first in range(1, upper_limit):
    for second in range(1, upper_limit):
        largest = max(first, second)
        for third in range(first_small, l + first_small):
            third = chr(third)
            for fourth in range(first_small, l + first_small):
                fourth = chr(fourth)
                for fifth in range(largest + 1, upper_limit):
                    print(f'{first}{second}{third}{fourth}{fifth}', end=' ')
