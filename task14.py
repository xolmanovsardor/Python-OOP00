class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} yoshda.")

# Test
students = [
    Student("Ali", 15),
    Student("Malika", 17),
    Student("John", 16),
    Student("Sara", 18),
    Student("Bob", 14)
]
oldest = max(students, key=lambda s: s.age)
oldest.show_info()
