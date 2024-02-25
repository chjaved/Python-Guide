# DICTIONARIES IN PYTHON : Dictionaries are used to store data values in key:value pairs. They are unordered, mutable & don't allow duplicate keys.
# In List, String, Tuples we have indexes(Orders) but in dictionary we dont have Indexes(NO ORDER).

# dict = {
#     "name": "Javed",
#     "age" : 19,
#     "city" : "Rwp",
#     "marks" : [98,97,95],
# }
# print(dict,type(dict))

# dict["key"]  ="value" # to assign or add new 

# Nested Dict : Dictionary inside a dictionary
# dict = {
#     "nested" : {
#         "name":"javed"
#     },
#     "name": "Javed",
#     "age" : 19,
#     "city" : "Rwp",
#     "marks" : [98,97,95],
# }
# print(dict["age"]) #it gives error if we write age1 or something else instead of age while if go for method means dict.get("age") it doesnot give error it just returns None.

# # DICTIONARY METHODS
# print(dict.keys()) #return all keys
# print(dict.values()) #return all values
# print(dict.items()) #return all (key,val) pairs as tuple
# # type casting
# print(dict.keys())
# print(len(list(dict.keys())))
# print(dict.get("name")) #return the key according to value
# dict.update({"city2" : "isb"}) #insert the specified items to the dicionary
# print(dict)
# ####### IMPORTANT #######
# List  = ["A","B"]
# Tuple = ("A","B")
# Dict  =  "dict" : {"A":"b"}
# Set   = {}


# SETS IN PYTHON: Sets is the collection of the unordered items. Each element in the set must be unique and immutable.
# We cannot store list and dictionaries in Sets but tuple can store in sets.
nums1 = {1,2,3,4}
nums2 = {9,1,3,6}
#set2 = {1,2,2,2} #Repeated elements stored only once, so it resolved to {1,2}, Dont give error but ignores duplicate values.
# null_set = set() #empty set syntax
# print(null_set)
# print(nums1,type(nums1))
# print(len(nums1)) # length also ignores duplicate values

# IMPORTANT : SET itself is mutable means we can add & remove something but the ELEMENTS in set is immutable we cannot change it. Setd contains hashable values, Means unhashable values are changeable or changed values
#SETS METHODS
# nums1.add(5) # adds an element #also we can pass tuple here but list and dict cannot be passed
# print(nums1)

# nums1.remove(3) # removes an element
# print(nums1)

# nums1.clear() # empties the set
# print(nums1)

# nums1.pop() # removes a random value
# print(nums1)

# #Union & Intersaction
 
# print(nums1.union(nums2))
# print(nums1.intersection(nums2))

# PRACTICE QUESTIONS

# Question 1: Store following word meanings in a python dictionary: table:"a peice of furniture", "list of facts & figures" cat: " a small animal"

# dict = {
#     "table": ["a peice of furniture","list of facts and figures"],
#     "cat" : "a small animal"
# }
# print(dict)

# Question 2: You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "Python","java","C++","python","javascript","java","python","java","C++","C"

# Subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(Subjects),Subjects)

# Question 3: Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
# dict = {}
# m1 = int(input("Enter marks of first subject"))
# dict.update({"subject1" : m1})
# print(dict)
# m2 = int(input("Enter marks of second subject"))
# dict.update({"subject2" : m2})
# print(dict)
# m3 = int(input("Enter marks of third subject"))
# dict.update({"subject3" : m3})
# print(dict)


# Question no 4: Figure out a way to store 9 & 9.0 as seperate value in the set (You can take help of built-in data types)
# method 1: make 1 integer and other same number a string
# method 2: Using built-in data type
set = {9,"9.0"}
values = {
    ("float",9.0),
    ("int",9),
}
print(values)
print(set)