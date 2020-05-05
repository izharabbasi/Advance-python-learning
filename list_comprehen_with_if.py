# Normal If statement with List

number = list(range(1, 11))
even_number = []
for num in number:
    if num % 2 == 0:
        even_number.append(num)

print(even_number)


# if statement with list comprehension

even_num = [num for num in range(1, 11) if num % 2 == 0]
print(even_num)

