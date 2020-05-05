def add_total(*args):
    mul = 1
    for num in args:
        mul *= num
    return mul


num = [1, 2, 4]
print(add_total(*num))
