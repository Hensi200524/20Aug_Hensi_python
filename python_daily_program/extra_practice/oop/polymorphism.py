class Dog:
    def make_sound(self):
        print("Dog barks")

class Cat:
    def make_sound(self):
        print("Cat meows")

class Cow:
    def make_sound(self):
        print("Cow moos")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()
