numbers = list(map(int, input().split(' ')))
n = int(input())

mult_list = []

for item in numbers:
    mult_list.append((item * n))

for elem in mult_list:
    print(elem, end=' ')



