class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year):
        self.year = year
        self.make = make
        self.model = model

    def describe_car(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

mycar = Car("Toyota", "Corolla", 2020)
mycar.describe_car()

