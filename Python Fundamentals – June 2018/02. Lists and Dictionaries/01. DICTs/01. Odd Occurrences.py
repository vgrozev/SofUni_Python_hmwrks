raw_data = input()

data = raw_data.lower().split(" ")

dict_inputs = {}
string_output = ""

for item in data:
    if item in dict_inputs:
        dict_inputs[item] += 1
    else:
        dict_inputs[item] = 1

for i in dict_inputs:
    if dict_inputs[i] % 2 != 0:
        string_output += i + ", "

print(string_output.strip(", "))
