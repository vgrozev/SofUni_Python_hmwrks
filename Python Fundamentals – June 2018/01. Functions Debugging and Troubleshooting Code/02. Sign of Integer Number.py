number = int(input())


def sign_of_num(n):
    if number > 0:
        result = f"The number {n} is positive."
        return result

    elif number < 0:
        result = f"The number {n} is negative."
        return result

    else:
        result = f"The number {n} is zero."
        return result


print(sign_of_num(number))
