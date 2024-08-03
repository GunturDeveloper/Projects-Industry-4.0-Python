# Polimorfisme dalam OOP
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    return animal.sound()

cat = Cat()
dog = Dog()

print(make_sound(cat))
print(make_sound(dog))
