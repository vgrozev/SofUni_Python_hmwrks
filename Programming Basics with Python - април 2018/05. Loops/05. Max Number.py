n = int(input())
max_num = int(input())

for i in range(1, n):
    num = int(input())
    if num > max_num:
        max_num = num

print(max_num)
