raw_data = input()

dict_inputs = {}

while raw_data != "end":

    data = list(map(str.strip, raw_data.split("=")))
    dict_key = data[0]
    dict_value = data[1]

    if dict_value.isnumeric():
        dict_inputs[dict_key] = int(dict_value)
    else:
        value_to_replace = dict_inputs.get(dict_value)
        if value_to_replace:
            dict_inputs[dict_key] = value_to_replace

    raw_data = input()

for key in dict_inputs:
    print(f'{key} === {dict_inputs[key]}')