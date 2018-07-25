n = int(input())


# def line_dashes(size):
#     print("-" * (size * 2))
#
#
# def body(size):
#     for i in range(size - 2):
#         print("-" + "\\/" * int((2 * size - 2) / 2) + "-")

def line_dashes(size):
    print("-" * (size * 2))


def body(size):
    for i in range(size - 2):
        print("-" + "\\/" * (size - 1) + "-")


line_dashes(n)
body(n)
line_dashes(n)
