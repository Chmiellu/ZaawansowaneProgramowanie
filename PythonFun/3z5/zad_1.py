class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.passed = self.is_passed()

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Tomasz Chmiel", [60, 70, 80, 19])
student2 = Student("Robert Kubica", [40, 30, 45, 0, 11])

print(student1.name, "zdał semestr:", student1.passed)
print(student2.name, "zdał semestr:", student2.passed)
