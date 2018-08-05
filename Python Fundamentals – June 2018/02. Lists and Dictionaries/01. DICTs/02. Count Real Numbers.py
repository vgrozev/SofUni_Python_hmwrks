raw_data = input()

data = list(map(float, raw_data.split()))
dict_inputs = {}

for item in data:
    if item in dict_inputs:
        dict_inputs[item] += 1
    else:
        dict_inputs[item] = 1


for item in sorted(dict_inputs.keys()):
    print(F'{item} -> {dict_inputs[item]} times')

