def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

my_list = [5, 10, 15, 20]
result = sum_of_list(my_list)
print(f"The sum of {my_list} is {result}.")
