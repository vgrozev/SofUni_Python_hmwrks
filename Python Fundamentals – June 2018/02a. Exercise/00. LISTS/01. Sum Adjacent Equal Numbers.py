data = list(map(float, input().split()))

i = 0
while i < (len(data) - 1):
    if data[i] == data[i + 1] and i >= 0:
        data[i] += data[i + 1]
        data.remove(data[i + 1])
        i -= 1
    else:
        i += 1

# print(*data)
# for item in data:
#     print("{0:g}".format(item), end=' ')

# print(" ".join('%g' % item for item in data))

print(" ".join(["{:g}".format(item) for item in data]))

