def add(*args):
    return args


print(add(2, 3, 3, 4, 5))


def total_num(*args):
    total = 0
    for num in args:
        total += num
    return total


print(total_num(1, 2, 3))
