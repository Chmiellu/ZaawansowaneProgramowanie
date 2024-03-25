class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.passed = self.is_passed()

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50



