class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
def info(self):
    print(f"o'quvchi haqida malumot: Ismi{self.name} Yoshi{self.age},  {self.grade} - Sinf o'quvchisi")
s01 = Student('Ali', 20, 'A')
s01.info()