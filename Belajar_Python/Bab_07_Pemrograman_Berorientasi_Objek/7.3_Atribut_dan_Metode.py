# Atribut dan metode dalam kelas
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.model}"

car = Car("Toyota", 2022)
print(car.description())
