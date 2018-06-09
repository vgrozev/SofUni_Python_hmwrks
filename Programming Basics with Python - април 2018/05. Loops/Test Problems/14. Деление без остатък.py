n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0

for i in range(0, n):
    input_num = int(input())

    if input_num % 2 == 0:
        p1_count += 1
    if input_num % 3 == 0:
        p2_count += 1
    if input_num % 4 == 0:
        p3_count += 1

p1 = (p1_count / n) * 100
p2 = (p2_count / n) * 100
p3 = (p3_count / n) * 100

print('{:.2f}%'.format(p1))
print('{:.2f}%'.format(p2))
print('{:.2f}%'.format(p3))

