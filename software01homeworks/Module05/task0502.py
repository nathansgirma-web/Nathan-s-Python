numbers = []
number = int(input("Enter a number or quit by pressing enter: "))
while number != "":
    number = int(number)
    numbers.append(number)
    number = int(input("Enter a number or quit by pressing enter: "))
numbers.sort(reverse=True)
print("The five great numbers are: ")
for i in numbers[:5]:
    print(i)
