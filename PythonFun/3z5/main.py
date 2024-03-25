from classes.zad_1 import Student
from classes.zad_4 import fetch_breweries
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    args = parser.parse_args()
    breweries = fetch_breweries(city=args.city)
    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()


student1 = Student("Tomasz Chmiel", [60, 70, 80, 19])
student2 = Student("Robert Kubica", [40, 30, 45, 0, 11])

print(student1.name, "zdał semestr:", student1.passed)
print(student2.name, "zdał semestr:", student2.passed)