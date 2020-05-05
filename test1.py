#In this test I convert int or float data type in string

def convert_string(list1):
    return [str(i) for i in list1 if (type(i)== int or type(i) == float)]

print(convert_string([11.23,34,343.2]))