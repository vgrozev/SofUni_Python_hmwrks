num = int(input())
count = 0
if num > 1000:
    count = num * 0.1
elif num > 100:
    count = num * 0.2
elif num <= 100:
    count = count + 5

if num % 2 == 0:
    count = count + 1

if num % 10 == 5:
    count = count + 2

print(count)
print(count + num)
