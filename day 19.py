
class Car:
    def __init__(self):
        self.brand = 'MG'
        self.cost = 8.70
        self.colour = 'Blue'

    def start_engine(self):
        print(self.brand, 'engine is starting')

    def start_gear(self):
        print(self.brand, 'shifting gear')

    def accelerate(self):
        print(self.brand, 'car is accelerating')


# Creating an object
c1 = Car()

# Accessing attributes
print(c1.brand)
print(c1.cost)
print(c1.colour)

# Calling methods
c1.start_engine()
c1.start_gear()
c1.accelerate()
