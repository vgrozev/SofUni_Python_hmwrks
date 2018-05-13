num = int(input())

first_digit = num // 10
second_digit = num % 10
final_string = ''

if num == 100:
    final_string = "one hundred"
elif num == 0:
    final_string = "zero"
elif 10 <= num < 20:
    # 1 to 19 #########################################
    if num == 10:
        final_string = "ten"
    elif num == 11:
        final_string = "eleven"
    elif num == 12:
        final_string = "twelve"
    elif num == 13:
        final_string = "thirteen"
    elif num == 14:
        final_string = "fourteen"
    elif num == 15:
        final_string = "fifteen"
    elif num == 16:
        final_string = "sixteen"
    elif num == 17:
        final_string = "seventeen"
    elif num == 18:
        final_string = "eighteen"
    elif num == 19:
        final_string = "nineteen"
elif (20 <= num < 100) or (0 < num < 10):
    # 20 to 99 ending on 0 ##########################
    if first_digit == 0:
        final_string = ''
    elif first_digit == 2:
        final_string = 'twenty'
    elif first_digit == 3:
        final_string = 'thirty'
    elif first_digit == 4:
        final_string = 'forty'
    elif first_digit == 5:
        final_string = 'fifty'
    elif first_digit == 6:
        final_string = 'sixty'
    elif first_digit == 7:
        final_string = 'seventy'
    elif first_digit == 8:
        final_string = 'eighty'
    elif first_digit == 9:
        final_string = 'ninety'

    # 20 to 99 NOT ending on 0 ##########################
    if num > 20 and second_digit != 0:
        final_string = final_string + ' '

    if second_digit == 1:
        final_string = final_string + 'one'
    elif second_digit == 2:
        final_string = final_string + 'two'
    elif second_digit == 3:
        final_string = final_string + 'three'
    elif second_digit == 4:
        final_string = final_string + 'four'
    elif second_digit == 5:
        final_string = final_string + 'five'
    elif second_digit == 6:
        final_string = final_string + 'six'
    elif second_digit == 7:
        final_string = final_string + 'seven'
    elif second_digit == 8:
        final_string = final_string + 'eight'
    elif second_digit == 9:
        final_string = final_string + 'nine'
else:
    final_string = "invalid number"

print(final_string)

#############################################################################################
# second solution using lists

# to_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#
# tens_to_90 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#
# num = int(input())
#
#
# if 0 <= num < 20:
#     print(to_19[num])
# elif 20 <= num <= 100:
#     if num == 100:
#         print('one hundred')
#     elif num % 10 == 0:
#         print(tens_to_90[num // 10])
#     else:
#         print(tens_to_90[num // 10], to_19[num % 10])
# else:
#     print('invalid number')
