from abc import ABC, abstractmethod # import abstract class
 
class Animal(ABC): # main or parent class
 
    @abstractmethod #abstract method
    def leg(self):
        pass
    
    def output(self): # concrete method
        print("this is abstract class not interface")
 
class Cow(Animal): # child class of Animal
 
    def leg(self): # overriding abstract method
        print("Cow has 4 legs")

class Bat(Animal): # child class of Animal
 
    def leg(self): # overriding abstract method
        print("Bat has 2 legs")
    
cow = Cow() # object of Cow class
bat = Bat() # object of Bat class

cow.leg() # function call of Cow class
bat.leg() # function call of Bat class