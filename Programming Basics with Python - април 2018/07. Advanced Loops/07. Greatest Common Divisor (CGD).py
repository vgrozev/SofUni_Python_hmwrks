a = int(input())
b = int(input())

while not b == 0:
    temp = b
    b = a % b
    a = temp

print(a)