num = int(input())


for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if num % first == 0 and num % second == 0 and num % third == 0 and num % fourth == 0:
                    print(f'{first}{second}{third}{fourth}', end=' ')
