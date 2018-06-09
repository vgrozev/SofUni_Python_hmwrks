n = int(input())

odd_sum = 0
odd_min = 1000000000.0
odd_max = -1000000000.0
even_sum = 0
even_min = 1000000000.0
even_max = -1000000000.0

if n == 0:
    odd_min = 'No'
    odd_max = 'No'
    even_min = 'No'
    even_max = 'No'
elif n == 1:
    one = float(input())
    odd_sum = one
    odd_min = one
    odd_max = one
    even_min = 'No'
    even_max = 'No'
else:
    for i in range(1, (n + 1)):
        number = float(input())
        if (i % 2) == 0:
            even_sum += number
            if number < even_min:
                even_min = number
            if number > even_max:
                even_max = number
        else:
            odd_sum += number
            if number < odd_min:
                odd_min = number
            if number > odd_max:
                odd_max = number

# fix the trailing zerows, if value is not 'No'
if type(odd_min) != str:
    odd_min = format(float(odd_min), 'g')
if type(odd_max) != str:
    odd_max = format(float(odd_max), 'g')
if type(even_min) != str:
    even_min = format(float(even_min), 'g')
if type(even_max) != str:
    even_max = format(float(even_max), 'g')

print("OddSum = {:g}".format(odd_sum))
print("OddMin =", odd_min)
print("OddMax =", odd_max)
print("EvenSum = {:g}".format(even_sum))
print("EvenMin =", even_min)
print("EvenMax =", even_max)

