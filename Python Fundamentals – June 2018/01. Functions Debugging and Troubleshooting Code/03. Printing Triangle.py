n = int(input())


def print_triangle(inp_num):
    for i in range(inp_num):
        for j in range(1, i + 2):
            print(f'{j} ', end='')

        print()

    for i in range(inp_num - 1, 0, -1):
        for j in range(1, i + 1):
            print(f'{j} ', end='')

        print()


print_triangle(n)
