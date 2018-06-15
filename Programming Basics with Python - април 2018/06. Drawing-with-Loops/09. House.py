n = int(input())

roof_size = (n + 1) // 2
house_size = n // 2
house_body = '|' + '*' * (n - 2) + '|'

if n % 2 == 0:
    stars = 2
else:
    stars = 1

for i in range(roof_size):
    dashes = '-' * ((n - stars) // 2)
    print(dashes + '*' * stars + dashes)
    stars += 2

for j in range(house_size):
    print(house_body)

