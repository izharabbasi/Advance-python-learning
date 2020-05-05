#Nested if statement with list comprehension
#example = [[1,2,3],[1,2,3],[1,2,3]]


nested_num = [[i for i in range(1,4)] for num in range(3)]
print(nested_num)