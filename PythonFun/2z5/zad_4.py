def check_sum(num1: int, num2: int, num3: int) -> bool:
    if num1 + num2 >= num3:
        return True
    else:
        return False


print(check_sum(2, 3, 6))
