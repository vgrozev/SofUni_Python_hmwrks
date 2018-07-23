num = int(input())

a = 0
b = 1

if num < 2:
    out = 1
else:
    for i in range(num):
        b = a + b
        a = b - a

print(b)
