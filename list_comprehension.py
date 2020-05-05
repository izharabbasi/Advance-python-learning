# Normal reverse function with list


def str_reverse(list1, list2):
    name = []
    name2 = []
    for i in list1:
        name.append(i[::-1])
    for j in list2:
        name2.append(j[::-1])
    return name, name2


print(str_reverse(["izhar", "sheryar"], ["ahmed", "umair"]))

# Reverse Function with List comprehension


def str_reverse1(list1, list2):
    name1 = [name[::-1] for name in list1]
    name2 = [name[::-1] for name in list2]
    return name1, name2


print(str_reverse(["izhar", "shery"], ["ahmed", "umair"]))
