# Pewarisan dalam OOP
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

dog = Dog()
print(dog.speak())
print(dog.bark())
