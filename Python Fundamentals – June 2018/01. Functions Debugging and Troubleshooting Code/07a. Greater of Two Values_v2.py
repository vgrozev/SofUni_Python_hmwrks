input_type = input()
val_1 = input()
var_2 = input()


def compare_values(a, b):
    if a > b:
        return a
    else:
        return b


def get_grater_value(inp_t, v_1, v_2):
    if inp_t == 'int':
        return compare_values(int(v_1), int(v_2))

    elif inp_t == 'char':
        return chr(compare_values(ord(v_1), ord(v_2)))

    else:
        return compare_values(v_1, v_2)


result = get_grater_value(input_type, val_1, var_2)
print(result)
