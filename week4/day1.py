# class Car:
#     #class attributes => constant to the entire object created
#     wheels = 4
#     comments = "satisfactory"
#     #constructor method
#     #instant attributes
#     def __init__(self, color,make,year):
#         self.color = color
#         self.make = make
#         self.year = year
#         pass

# car1 = Car("Black","Benz", 2024)

# car2 = Car("white", "volvo", 1995)


#methods
# class Car:
#     #class attributes => constant to the entire object created
#     wheels = 4
#     comments = "satisfactory"
#     #constructor method
#     #instant attributes
#     def __init__(self, color,make,year):
#         self.color = color
#         self.make = make
#         self.year = year

    
#     def describe(self):
#         return(f"This is a {self.color} , {self.year}, {self.make}")


# Car1 = Car("Black","Benz", 2024)


# print(Car1.describe())



#inheritance => A class takes on the methods and attributes of another class

class Car:    
    wheels = 4
    comments = "satisfactory"
    #constructor method
    #instant attributes
    def __init__(self, color,make,year):
        self.color = color
        self.make = make
        self.year = year

    def describe(self):
        return(f"This is a {self.color} , {self.year}, {self.make}")

class ElectricCar(Car):
    def __init__(self, color, make, year,battery ):
        super().__init__(color, make, year, )
        self.battery = battery

    def describe_electric(self):
        return(f"This is a {self.color}, {self.make}, {self.year} , with a {self.battery}")
    

car1 = ElectricCar("Red","subaru", 1996 ,1500)
print(car1.describe_electric())
print(car1.describe())