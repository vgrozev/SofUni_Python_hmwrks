n = int(input())

print('+ ' + '- ' * (n - 2) + '+')

for i in range(n - 2):
    print('| ' + '- ' * (n - 2) + '|')

print('+ ' + '- ' * (n - 2) + '+')
