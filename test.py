text = input()
lower_case = []
upper_case = []
mixed = []
replacements = (',', ';', ':', '. ', '!', '(', ')', '"', "'", '\\', '/', '[', ']', "''", '  ', " .", '.')
for r in replacements:
    text = text.replace(r, ' ')
print(text)
words = [word for word in text.split()]
for word in words:
    if word == word.lower() and word.isalpha() == True:
        lower_case.append(word)
    elif word == word.upper() and word.isalpha() == True:
        upper_case.append(word)
    else:
        mixed.append(word)

print('Lower-case: ' + ', '.join(lower_case))
print('Mixed-case: ' + ', '.join(mixed))
print('Upper-case: ' + ', '.join(upper_case))