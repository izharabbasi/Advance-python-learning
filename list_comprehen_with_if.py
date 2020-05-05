# Normal If statement with List

number = list(range(1, 11))
even_number = []
for num in number:
    if num % 2 == 0:
        even_number.append(num)

print(even_number)


# if statement with list comprehension
digit = [1,2,3,4,5,6,7,8,9,10]
even_num = [num for num in digit if num % 2 == 0]
print(even_num)

odd_num = [num for num in range(1,11) if num %2==1]
print(odd_num)
