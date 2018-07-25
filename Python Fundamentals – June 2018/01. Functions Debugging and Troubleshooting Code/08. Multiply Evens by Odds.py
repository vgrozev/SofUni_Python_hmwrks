n = int(input())


def even_sum(num):
    e_sum = 0
    while num > 0:
        if (num % 10) % 2 == 0:
            e_sum += num % 10

        num = num // 10

    return e_sum


def odd_sum(num):
    o_sum = 0
    while num > 0:
        if (num % 10) % 2 != 0:
            o_sum += num % 10

        num = num // 10

    return o_sum


def even_by_odd_multip(integer_n):
    num = abs(integer_n)

    evn_sm = even_sum(num)
    odd_sm = odd_sum(num)

    return evn_sm * odd_sm


result = even_by_odd_multip(n)
print(result)
