magic_num = int(input())


for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                for fifth in range(1, 10):
                    for sixth in range(1, 10):
                        if first * second * third * fourth * fifth * sixth == magic_num:
                            print(f'{first}{second}{third}{fourth}{fifth}{sixth}', end=' ')
