"""LOOPS IN PYTHON"""
#For LOOPS
#While Loops
#There is no do while loop in Python
#Loops are used to repeat instructions.

"""WHILE LOOP"""
"""STRUCTURE: 
            #while Loops
            while condition:
                #Some Work    
"""
# while True:
#     print("HelloWorld") #Infinite Loop
# count =  1 #Iterators : variables that we used for iteration
# while count<=10:
#     print("hello" , count)
#     count+=1 # oposite loop count-=1 & variable should be greater

"""LETS PRACTICE"""
# Question 1:Print numbers from 1 to 100
# n = 1
# while n <= 100:
#     print(n)
#     n += 1

# Question 2:Print numbers from 100 to 1
# n = 100
# while n >= 1:
#     print(n)
#     n -= 1

#Question 3: Print the multiplication table of number n.
# n = int(input("Enter the number to print its table"))
# i=1
# while i <=10:
#     print(n,"x",i,"=",n*i)
#     i+=1

#Question 4: Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100] #square of numbers from 1-10
# traverse:traveling the element of list, tuple or any other datatype one-by-one.
# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx+=1

#Question 5: Search for a number x in this tuple using loop:
# tup = (1,4,9,16,25,36,49,64,81,100,1)
# x = int(input("Enter the number to find"))
# i = 0
# while i <len(tup):
#     if(tup[i] == x):
#         print("Found")
#     else:
#         print("Finding...")
#     i+=1

"""BREAK & CONTINUE STATEMENTS"""
# i = 1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("End of loop")

# continue statement: terminates execution in the current iteration & continues execution of the loop with the next iteration.

#i=0
#while i<=10:
#    if(i%2 == 0): #Prints odd number || # Prints even numberif(i%2 != 0):
#        i+=1
#        continue #skip
#    print(i)
#    i +=1

"""FOR LOOPS"""
#for loops are used for sequential traversal.For traversing list, string, tuples etc.

# FOR LOOPS
"""
    for el on list:
        #some work
"""
# list = [1,2,3]

# for val in list:
#     print(val)
# FOR LOOPS WITH ELSE
"""
    for el in list:
        #some work
    else: # optional else
        #work when loops end
"""
# str = "JD"

# for char in str:
#     if(char=="J"):
#         print("J found")
#         break
# else:
#     print("END")

"""PRACTICE QUESTIONS"""

#Question 1: print the element of the following list using for loop : list = [1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# for val in list:
#     print(val)

# Question 2: Search for a number x in this tuple uing for loop: tup = ( 1,4,9,16,25,36,49,64,81,100)
# """LINEAR SEARCH : element by element single line search"""
# tup = (16,4,9,16,25,36,49,64,81,100,16)
# for val in tup:
#     if (val == 16):
#         print("Found",val)
#         break
#     else:
#         print("not found")

#RANGE FUNCTION : range() : Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

#range(start? ,stop, step?)

# for el in range(5): #(1,5) #(1,10,3) = gape of 3
#     print(el)

"""PRACTICE QUESTIONS : using for & range()"""
#Question 1: Print number from 1 to 100
# for el in range (1, 101):
#     print(el)

#Question 2:print number form 100 to 1
# for el in range(101,0, -1): # step size negative for decreasing order
#     print(el)

#Question 3: Print the multiplication table of a number n.
# n =  int (input("Enter the number to print "))
# for val in range(1, 11):
#     print(val,"x",n,"=",val*n)

"""PRACTICE QUESTIONS"""
#Question 1: Write a program to find the sum of first n (natural numbers) numbers (using while).

# n = int(input("Enter the number")) # 5 entered = 1+2+3+4+5 = 15
# sum = 0
# i = 1
# while i<=n:
#     sum = sum + i
    
#     i+=1
# print(sum)

#Question 2: Writea program to find the factorial of first n (natural numbers) numbers. (using for)
n = int(input("Enter the number")) # 5 entered = 1+2+3+4+5 = 15
fact = 1
i = 1
while i<=n:
    fact *=  i
    i+=1
print(fact)

