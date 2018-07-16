n = int(input())
result = 1

for i in range(0, n + 1):
    print(result)
    result = result * 2 + 1

    if result > n:
        break
