def multiply_for_loop(numbers):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num * 2)
    return multiplied_numbers

def multiply_list_comprehension(numbers):
    return [num * 2 for num in numbers]

numbers = [33, 129, 999999, 23.23, -3.2]
print("Using for loop:", multiply_for_loop(numbers))
print("Using list comprehension:", multiply_list_comprehension(numbers))
