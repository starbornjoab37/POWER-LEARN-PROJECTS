#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism
class Human():
    def __init__(self,nam,age):
        self.name= "name"
        self.age ="age"
class adult(Human):
    def  move(self):
        print("Adult is walking") 
    def communicate(self):
        print("Adult is talking")

class baby(Human):
                                     
    def  move(self):
        print("Baby is crawling")

    def communicate(self):
        print("Baby is crying")

my_child = baby("Jea",2)
my_mom = adult("Anna",30)
my_mom.move()
my_child.communicate()


# Create a program that includes animals or vehicles with the same action (like move()). 
class Transport:
    def __init__(self, model, color):
        self.model = model
        self.color = color

# However, make each class define move() differently (for example, Car.move() prints 
# "Driving" 🚗, while Plane.move() prints "Flying" ✈️)
class Car(Transport):
    def move(self):
        print("Driving 🚗")

class Plane(Transport):
    def move(self):
        print("Flying ✈️")

# Testing the classes
my_car = Car("Toyota", "Red")
my_plane = Plane("Boeing", "White")

my_car.move()
my_plane.move()
