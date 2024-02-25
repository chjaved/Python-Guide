"""OBJECT ORIENTED PROGRAMMING"""
# To map with real world scenarios, we started using object in code. This is called object oriented programming.

# Class : is a blueprint for creating objects.
# class student:
#     name = "JD"

# # creating object (instance)
# s1 = student()
# print(s1.name)

# s2 = student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# CONSTRUCTOR: Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
# if we dont write init funtion, python automatically creates it.

# Creating Class
# attributes are the data or variables we use inside a class
# class Student():

    # """If we have more than one constructor in the class than the constructor whose parameters matches will be executed"""
    #DEFAULT CONSTRUCTOR : haing self only
    # def __init__(self):
    #     print("This is a default constructor")

    # PARAMETERIZED CONSTRUCTOR
#     def __init__(self,name, marks): # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#         self.name = name # instance attributes
#         self.marks = marks # instance attributes

# #creating object
# s1 = Student("JD", 78)
# print(s1.name, s1.marks)
# s2 = Student("JD2", 88)
# print(s2.name, s2.marks)

# CLASS ATTRIBUTES : common for whole class and all objects  & INSTANCE ATTRIBUTES: are different for each object
# Class.attr : 
# obj.attr"

# class Student:
#     # college name : class attribute
#     # students name : instance attributes
#     college_name = "NUML" #class attribute
#     # name = "anonymous"
#     def __init__(self,name, marks): 
#         self.name = name # instance attributes
#         self.marks = marks # instance attributes precedense is always higher than class atrribute when same names.

# s1 = Student("JD", 78)
# print(s1.name, s1.marks)
# s2 = Student("JD2", 88)
# print(s2.name, s2.marks)

# print(Student.college_name)

"""CLASS IS THE COLLECTION OF DATA, OBJECT (Properties) OF METHODS (Functions or workings of objects)"""
# METHODS: Methods are functions that belongs to objects.(Functions inside the classes are normally known as methods)

# class Student:
#     college_name = "NUML Rwp"
#     #Constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         # Creating Method
#     def welcome(self):
#         print("welcome student", self.name)

#     def getMarks(self):
#         return self.marks


# s1 = Student("JD" , 97)
# print(s1.name)
# print(s1.getMarks())
# s1.welcome()

"""PRACTICE QUESTIONS"""
# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:
#     def __init__(self, name, marks): # assuming marks as list
#         self.name = name #attribute
#         self.marks = marks

#     def average(self):
#         sum = 0
#         for val in self.marks:
#             sum+= val
#         print("hi", self.name, "average", sum/3)

        
# s1 = Student("JD", [95,97,94])
# s1.average()

# STATIC METHODS : Methods that dont use the self parameter (work at class level)
"""class Student
    @staticmethod #decorator: Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanentlty modifying it.
    def college():
    print ("ABC College")
"""