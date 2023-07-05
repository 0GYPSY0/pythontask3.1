
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print( f"Hi {self.name} you are {self.age} years old now, Congrats")
person1 = Person ("radha", 3)
person2 = Person ("devan", 1)

person1.greet()
person2.greet()