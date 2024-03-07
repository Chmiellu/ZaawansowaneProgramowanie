import random


def display_every_second_element(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])


numbers = random.sample(range(0, 999), 10)
print(f"All numbers {numbers}")
print("Every second element:")
display_every_second_element(numbers)
