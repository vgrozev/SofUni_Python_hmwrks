input_type = input()
val_1 = input()
var_2 = input()


def get_grater_value(inp_t, v_1, v_2):
    if inp_t == 'int':
        if int(v_1) > int(v_2):
            return v_1
        else:
            return v_2
    elif inp_t == 'char':
        if ord(v_1) > ord(v_2):
            return v_1
        else:
            return v_2
    else:
        if v_1 > v_2:
            return v_1
        else:
            return v_2


print(get_grater_value(input_type, val_1, var_2))
