n = int(input())

frame_distance = ' ' * n
frame = '*' * (2 * n)
glass = '*' + '/' * (2 * n - 2) + '*'
bridge = '|' * n

print(frame + frame_distance + frame)

for i in range(n - 2):
    if ((n - 1) // 2) - 1 == i:
        print(glass + bridge + glass)
    else:
        print(glass + frame_distance + glass)

print(frame + frame_distance + frame)

