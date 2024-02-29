class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}\nOpen hours: {self.open_hours}\nPhone: {self.phone}\n"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\nAddress: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}\n"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book in Library: {self.library}\nPublication Date: {self.publication_date}\nAuthor: {self.author_name} {self.author_surname}\nNumber of Pages: {self.number_of_pages}\n"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"{book}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for student {self.student}\nOrdered books:\n{book_list}\nOrder Date: {self.order_date}\n"


library1 = Library("New York", "Main Street", "10001", "9:00 AM - 5:00 PM", "+1-123-456-7890")
library2 = Library("Los Angeles", "Broadway", "90001", "10:00 AM - 6:00 PM", "+1-987-654-3210")

employee1 = Employee("John", "Doe", "2023-01-15", "1990-05-25", "New York", "Park Avenue", "10002", "+1-111-222-3333")
employee2 = Employee("Jane", "Smith", "2023-02-20", "1988-08-10", "Los Angeles", "Sunset Boulevard", "90003", "+1-444-555-6666")
employee3 = Employee("Alice", "Johnson", "2023-03-25", "1995-11-12", "New York", "Broadway", "10004", "+1-777-888-9999")

book1 = Book(library1, "2022-12-01", "John", "Doe", 200)
book2 = Book(library1, "2022-11-15", "Alice", "Johnson", 150)
book3 = Book(library2, "2022-10-20", "Jane", "Smith", 300)
book4 = Book(library2, "2022-09-25", "John", "Doe", 250)
book5 = Book(library2, "2022-08-30", "Alice", "Johnson", 180)

order1 = Order(employee1, "Student1", [book1, book3, book5], "2023-04-01")
order2 = Order(employee2, "Student2", [book2, book4], "2023-04-05")

print(order1)
print(order2)
