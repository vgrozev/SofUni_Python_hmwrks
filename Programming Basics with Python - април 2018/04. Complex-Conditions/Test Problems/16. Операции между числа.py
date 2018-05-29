N1 = int(input())
N2 = int(input())
operator = input()

if N2 == 0:
    result = "Cannot divide {} by zero".format(N1)
elif operator == "/":
    result = "{0} / {1} = {2:.2f}".format(N1, N2, N1 / N2)
elif operator == "%":
    result = "{} % {} = {}".format(N1, N2, N1 % N2)
else:
    calc = eval(str(N1) + operator + str(N2))
    if calc % 2 == 0:
        calc_property = 'even'
    else:
        calc_property = 'odd'
    result = "{} {} {} = {} - {}".format(N1, operator, N2, calc, calc_property)

print(result)
