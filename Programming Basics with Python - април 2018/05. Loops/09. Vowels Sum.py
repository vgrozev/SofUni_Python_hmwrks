tekst = input()
str_sum = 0

for i in range(1, len(tekst)):
    if tekst[i] == 'a':
        str_sum += 1
    elif tekst[i] == 'e':
        str_sum += 2
    elif tekst[i] == 'i':
        str_sum += 3
    elif tekst[i] == 'o':
        str_sum += 4
    elif tekst[i] == 'u':
        str_sum += 5

print(str_sum)
