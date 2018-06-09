n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(0, n):
    input_num = int(input())

    if input_num < 200:
        p1_count += 1
    elif 200 <= input_num < 400:
        p2_count += 1
    elif 400 <= input_num < 600:
        p3_count += 1
    elif 600 <= input_num < 800:
        p4_count += 1
    else:
        p5_count += 1

p1 = (p1_count / n) * 100
p2 = (p2_count / n) * 100
p3 = (p3_count / n) * 100
p4 = (p4_count / n) * 100
p5 = (p5_count / n) * 100

print('{:.2f}%'.format(p1))
print('{:.2f}%'.format(p2))
print('{:.2f}%'.format(p3))
print('{:.2f}%'.format(p4))
print('{:.2f}%'.format(p5))
