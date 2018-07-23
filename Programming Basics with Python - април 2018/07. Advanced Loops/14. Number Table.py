n = int(input())

for i in range(0, n):

    for j in range(0, n):

        num = (i + j + 1)
        if num <= n:
            print(num, end=' ')

        else:
            num = 2*n - num
            print(num, end=" ")

    print("")
