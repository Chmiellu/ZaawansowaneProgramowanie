class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: area - {self.area}, rooms - {self.rooms}, price - {self.price}, address - {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)

    def __str__(self):
        return (
            f"House: area - {self.area}, rooms - {self.rooms}, price($) - {self.price}, address - {self.address}, "
            f"plot - {self.plot}"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat: area - {self.area}, rooms - {self.rooms}, price($) - {self.price}, address - {self.address}, "
            f"floor - {self.floor}"
        )


my_house = House(area=150, rooms=5, price=300000, address="123 Main St", plot=500)
my_flat = Flat(area=80, rooms=3, price=200000, address="456 Elm St", floor=2)

print(my_house)
print(my_flat)
