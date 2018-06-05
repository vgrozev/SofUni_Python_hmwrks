n = int(input())
min_num = int(input())

for i in range(1, n):
    num = int(input())
    if num < min_num:
        min_num = num

print(min_num)
