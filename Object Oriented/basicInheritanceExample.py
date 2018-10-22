'''
Classes can inherit from other classes. A class can inherit attributes and behaviour methods from another class, called the superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class.
'''


class Person:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print("My name is {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, heroName):
        self.heroName = heroName
        super().__init__(name)

    def printName(self):
        super().printName()
        print("..and I am {}".format(self.heroName))


if __name__ == "__main__":
    c = Person("Prath")
    c.printName()
    d = SuperHero("Prath", "PooPatel")
    d.printName()
