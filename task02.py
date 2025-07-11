class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Test
s1 = Student("Ali", 15, "9-sinf")
s2 = Student("Malika", 16, "10-sinf")
s3 = Student("John", 14, "8-sinf")

print(s1.name, s1.age, s1.grade)
print(s2.name, s2.age, s2.grade)
print(s3.name, s3.age, s3.grade)
