# #polymorphism
# #allow objects from differnt calsses treated as the same
# A = [1,2,3,4]
# B = ["MON", "TUE","WED"]
# print(len(A))

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print("woof")


# class Cat(Animal):
#     def speak(self):
#         print("meow")

# print(Cat().speak())



# animals = [Dog(), Cat()]

# for i in animals:
#     i.speak()
    



#abstracting => hides the complexity of abstract class
# from abc import ABC

# class shape(ABC) :
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         print(3.142 * self.radius * self.radius)


#unit testing
import unittest

# def add_numbers(a,b):
#     return a +b  
# print(add_numbers(1,2))  

# class Test_add_functions(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(add_numbers(1,7),4)
# if __name__ == "__main__":
#     unittest.main()


def look_for(a,collection):
    if a in collection:
        return True
    else:
        return False
# print(look_for(4,(2,3,4)))

# class Test_lookfor_in_collection(unittest.TestCase):
#     def test_lookfor(self):
#         self.assertIn(look_for(4 ,(7,8,9,4)),[True])
# if __name__ == "__main__":
#     unittest.main()


#unittest with strings
class Test_strings(unittest.TestCase):
    def test_lower(self):
        self.assertEqual("name".lower(), "Name")

if __name__ == "__main__":
    unittest.main()