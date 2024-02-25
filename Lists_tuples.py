# List in Python
# List is a built-in data type that stores a set of values, It can store elements of different types (Integer, Float, String, etc.) 
# strings are immutable(not changeable) in python while list are mutable (changeable)
# marks = [87,56,43,21,34]
# print(marks,type(marks), marks[0])
# student = ["JD",54,"UK"]
# student[0] = "Javed"
# len(student)
 
# # List Slicing : Similar to string slicing
# # list_name[starting_idx : ending_idx] #ending index is not included
# print(marks[1:4])

# # List Methods
# marks.append(4) #adds one element at the end
# print(marks) 
# marks.sort() #sort in ascending order
# print(marks)
# marks.reverse() #reverse list 
# print(marks) 
# marks.insert(1,5) #insert element at index 1
# print(marks) 
# marks.remove(56) #removes first occurence of given element
# print(marks)
# marks.pop(3) #removes element at idx
# print(marks)

# Tuples in Python : A built-in data type that let us create immutable sequence of values
# tup = (87,45,32,56,1,2,4,1,1)
# print(type(tup),tup,tup[0])
# tup[0] = 43 # Not allowed in Python
# tup1  = ()
# tup2 = (1,) #  creating a single valued tupple if not comma than interpreter thinks it as an integer/float not as tupple
# tup3 = (1,2,3)

# Tupple Slicing
# print(tup[1:3])

# # Tuple Methods
# print(tup.index(32))
# print(tup.count(1))

# Practice Excercise

# Write a program tp ask the user to enter names of their 3 favourite movies & store them in a list.
# mov1 = input("Enter first movie name")
# mov2 = input("Enter second movie name")
# mov3 = input("Enter third movie name")
# list = [mov1,mov2,mov3]
# print(list)

# Write a program to check if a list contains a palindrome of elements. (Hint use copy() method) [1,2,3,2,1] [1,"abc","abc",1]
# list = [1,2,3,2,1] #Copy and then reverse if same to original it is palindrome
# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not a palindrome")

# Write a program to count the number of students with the "A" grade in the following tuple. ["C","D","A","A","B","B","A"]
# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))
# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)
