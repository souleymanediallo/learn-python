def add(n_1, n_2):
    return n_1 + n_2


def calculator(n_1, n_2, func):
    return func(n_1, n_2)


result = calculator(2, 2, add)
print(result)


