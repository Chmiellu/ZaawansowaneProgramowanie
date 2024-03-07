def check_if_even(n) -> bool:
    if n % 2 != 0:
        return False
    else:
        return True


result = check_if_even(993330)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
