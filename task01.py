from datetime import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.time = datetime.today()


p01 = Car('BMW', 'M60', 2010)

print(p01.brand, p01.model, p01.year, p01.time)