num = int(input())

count = 0

for i in range(0, num):

    for j in range(0, i + 1):

        count += 1
        print(count, end=' ')

        if count == num:
            break

    if count == num:
        break
    print("")
