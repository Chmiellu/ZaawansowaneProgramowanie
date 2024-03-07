def hello(name: str, surname: str) -> str:
    if not isinstance(name, str) or not isinstance(surname, str):
        raise TypeError("Both 'name' and 'surname' must be strings.")
    return f"Cześć {name} {surname}!"


result = hello("Tomasz", "Chmiel")
print(result)
