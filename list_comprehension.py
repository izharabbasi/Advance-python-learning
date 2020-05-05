# Normal function with list

def str_reverse(list1,list2):
    name = []
    name2 = []
    for i in list1:
        name.append(i[::-1])
    for j in list2:
        name2.append(j[::-1])
    return name , name2

print(str_reverse(["izhar","sheryar"],["ahmed","umair"]))

