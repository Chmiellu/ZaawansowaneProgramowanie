import random
def display_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

numbers = random.sample(range(-1000, 2000), 10)
print(f"All numbers {numbers}")
print("Even numbers:")
display_even_numbers(numbers)

