data = list(map(int, input().split()))

# flip firs and last second and the one before last .. and so on. Loop just half of the list
for i in range(0, int(len(data)/2)):
    temp_int = data[-(i + 1)]
    data[-(i + 1)] = data[i]
    data[i] = temp_int

print(*data)