import classes.zad_1.Student

student1 = Student("Tomasz Chmiel", [60, 70, 80, 19])
student2 = Student("Robert Kubica", [40, 30, 45, 0, 11])

print(student1.name, "zdał semestr:", student1.passed)
print(student2.name, "zdał semestr:", student2.passed)