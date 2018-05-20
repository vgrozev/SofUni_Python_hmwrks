to_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens_to_90 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"]

num = int(input())

if 0 <= num < 20:
    print(to_19[num])
elif 20 <= num <= 100:
    if num % 10 == 0:
        print(tens_to_90[num // 10])
    else:
        print(tens_to_90[num // 10], to_19[num % 10])
else:
    print('invalid number')
