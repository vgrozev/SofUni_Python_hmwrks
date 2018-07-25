n = int(input())


def line_dashes(size):
    result = "-" * (size * 2)
    return result


def body(size):
    print(("-" + "\\/" * (size - 1) + "-" + '\n') * (size - 2), end='')


print(line_dashes(n))
body(n)
print(line_dashes(n))
