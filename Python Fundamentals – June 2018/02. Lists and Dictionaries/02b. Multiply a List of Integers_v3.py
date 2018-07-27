numbers = list(map(int, input().split(' ')))
n = int(input())

mult_list = []
index = 0

for item in numbers:
    mult_list.append((item * n))
    print(mult_list[index], end=' ')
    index += 1


