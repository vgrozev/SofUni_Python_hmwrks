data = input()

dict_inputs = {}

for item in data:
    if item in dict_inputs:
        dict_inputs[item] += 1
    else:
        dict_inputs[item] = 1

for item in dict_inputs:
    print(F'{item} -> {dict_inputs[item]}')
