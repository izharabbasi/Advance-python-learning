sqaure = {f"The sqaure of {num} is": num**2 for num in range(1, 11)}
print(sqaure)

for a, b in sqaure.items():
    print(f"{a} {b}")

name = "izhar"

string = {char: name.count(char) for char in name}
print(string)
