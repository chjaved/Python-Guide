"""FILE I/O IN PYTHON"""
#Python can be used to perform operations on a file. (read & write data)

# Types of all files
# 1. Text Files : .txt, .doxs, .log etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc  

"""OPERATIONS ON FILE"""

# OPEN, READ & CLOSE FILE
# f = open("file_name","mode") : mode is r: read mode & w: write mode | if not mode is written by default is read mode

# f = open("demo.txt", "r") # if not in same folder write complete path of file
# data = f.read() # read data
# print(data,type(data))
# f.close() # everytime close the file

"""SOME COMMON MODES"""
# 'r' : open for reading (default)
# 'w' : open for writting, truncating the file first
# 'x' : create a new file and open it for writing
# 'a' : open for writting, appending to the end of the file if it exists
# 'b' : binary mode
# 't' : text mode (default)
# '+' : open a disk file for updating (reading and writting)

# Once we read a data than it prints empty space
# f = open("demo.txt", "r") # if not in same folder write complete path of file
# data = f.read(5) # read 5 numbers f char f.readline() to read a line
# print(data,type(data))
# f.close() # everytime close the file

# WRITTING TO A FILE

# f = open("demo.txt","w")
# f.write("this is a new line") # Over writes the entire file

# f = open("demo.txt","a")
# f.write("this is a new line") # adds to the file

#when you want to open a file in 'a' or 'w' mode and it dosn't exists, python automatically creates a new file for you.
# f = open("JD.txt","a")
# f.write("Automaticaly Created")

# f = open("JD.txt","r+") # update the existing char from start
# f.write("Abc") #start reading after abc...
# f.close()

# DELETING A FILE: using the os module
# Modules (like a code library) is a file written by another programmer that generally a function we can use.

# import os : os = operating system
# os.remove("filename")

"""PRACTICE QUESTIONS"""
# Question 1: Create a new file "practice.txt" using python. Add the following data in it: .....
# with open("practice.txt", "r")  as f:
    # f.write("Hi everyone \n we are learning file I/O \n using Java. \n I like programming in Java")

# Question 2: Write a program that replace all occurrences of "Java" with python in above file.
#     content = f.read()
# modified_content = content.replace("Java", "Python")
# print(modified_content)
# with open("practice.txt", "w")  as f:
#     f.write(modified_content)

# Question 3: Search if the word "learning" exists in the file or not.
# word = "learning"
# with open("practice.txt", "r")  as f:
#     data = f.read()
#     if(data.find(word) != -1):
#        print("Found")
#     else:
#        print("Not Found")
   
# Question 4: Write a function to find in which line of the file does the word "learning" occurs first.

# Question 5: From a file containing numbers seperated by comma, print the count of even numbers.
