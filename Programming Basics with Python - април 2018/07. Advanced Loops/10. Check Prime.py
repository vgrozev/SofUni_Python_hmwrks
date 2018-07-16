import math

n = int(input())

is_prime = True


if n < 2:
    print('Not prime')
else:
    end_prob = int(math.sqrt(n))

    for i in range(2, end_prob + 1):
        if n / i == n // i:
            is_prime = False

    if is_prime:
        print('Prime')
    else:
        print('Not prime')
