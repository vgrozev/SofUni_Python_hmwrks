n = int(input())

leftRight = (n - 1) // 2
mid = n - 2 * leftRight - 2

for i in range((n - 1) // 2):
    if mid < 0:
        print('-' * leftRight + '*' + '-' * leftRight)
    else:
        print('-' * leftRight + '*' + '-' * mid + '*' + '-' * leftRight)

    leftRight -= 1
    mid += 2

for j in range((n + 1) // 2):

    if mid < 0:
        print('-' * leftRight + '*' + '-' * leftRight)
    else:
        print('-' * leftRight + '*' + '-' * mid + '*' + '-' * leftRight)

    leftRight += 1
    mid -= 2
