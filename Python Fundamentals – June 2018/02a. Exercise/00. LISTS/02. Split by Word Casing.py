# raw_data = input()
#
# lower_case_list = []
# mixed_case_list = []
# upper_case_list = []
#
# temp_list = []
#
# separator_list = [',', ';', ':', '.', '!', '(', ')', '"', '\'', '\\', '/', '[', ']']
#
# # remove all of the special characters, levin only the space separators
#
# for i in raw_data:
#     if i not in separator_list:
#         temp_list.append(i)
#
# # join it back to a whole string (not individual characters) and split it only by space
# temp_list = ''.join(temp_list).split()
#
# for word_str in temp_list:
#     if word_str == word_str.lower() and word_str.isalpha():
#         lower_case_list.append(word_str)
#     elif word_str == word_str.upper() and word_str.isalpha():
#         upper_case_list.append(word_str)
#     else:
#         mixed_case_list.append(word_str)
#
# print('Lower-case:', ', '.join(lower_case_list))
# print('Mixed-case:', ', '.join(mixed_case_list))
# print('Upper-case:', ', '.join(upper_case_list))


raw_data = input()
lower_case_list = []
upper_case_list = []
mixed_case_list = []

separator_list = [',', ';', ':', '.', '!', '(', ')', '"', '\'', '\\', '/', '[', ']']

for sep_char in separator_list:
    raw_data = raw_data.replace(sep_char, ' ')

temp_list = raw_data.split()
print(temp_list)
for item in temp_list:
    if item == item.lower() and item.isalpha():
        lower_case_list.append(item)
    elif item == item.upper() and item.isalpha():
        upper_case_list.append(item)
    else:
        mixed_case_list.append(item)

print('Lower-case:', ', '.join(lower_case_list))
print('Mixed-case:', ', '.join(mixed_case_list))
print('Upper-case:', ', '.join(upper_case_list))



