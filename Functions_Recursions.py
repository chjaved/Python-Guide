"""FUNCTIONS & RECURSIONS IN PYTHON"""
#FUNCTIONS: Block of statement that performs (inputs parameters and returns output) a specific task

"""STRUCTURE OF FUNCTION:
    def func_name(param1,param2..):  # function definition
        #some work
        return val

    func_name(arg1,arg2..) # function call

    1. Function can be without any parameter
    2. Function can also do not return any value OUTPUT : NONE
"""
#def sum(a,b): #Function definition | a & b are parameters
#    sum = a + b
#    print(sum)
#    return sum
#sum(2,3) #function calling
#sum(4,5)

# Average of 3 numbers
# def average(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg

# average(2,6,8)

"""TYPES OF FUNCTIONS"""
# 1. Built-in Functions (print(), len(), type(), rane(), etc)
# 2. User defined Functions

"""DEFAULT PARAMETERS"""
# Assigning a default value to parameter. which isused when no argument is passed
#def cal_prod(a,b = 1): # b is default argument, non-defaul argument should be comes first if we remove 1 from b it throws an error, ALWAYS START FROM LAST WHEN GIVING DEFAULT VALUES.
#    print(a*b) 
#    return a*b
#cal_prod(1)


"""PRACTICE QUESTIONS"""

#Question 1: Write a funtion to print the lengt of a list (list is the parameter)
# list = [2,3,4,5,5,2,3]
# def print_len(list):
#     print(len(list))
#     return len(list)

# print_len(list)

#Question 2: Write a function  to print the elements of a list in a a single line. (list is the parameter)
# list = [2,3,4,5,5,2,3]
# def print_elem(list):
#     for item in list:
#         print(item, end = " ")

# print_elem(list)
        

#Question 3: Write a function  to find the factorial of n. (n is the parameter)

# n = int(input("Enter the number to find its factorial"))
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         #recursive case: factorial of n is multiplied by factorial of (n-1)
#         return n * fact(n-1)
# print(fact(n))


#Question 4: Write a function to convert USD to PKR. 1 dollor = 279 pkr (current currency rate)
# amount = int(input("Enter amout to convert from USD to PKR"))
# def curr_convert(amount):
#     pkr = amount * 279
#     print(amount, "USD=",pkr,"PKR")
#     return pkr
# curr_convert(amount)

#Question 5: Write a program to take input from user and check if a number is odd it prints string "ODD" and if even it prints "EVEN".
# num = int(input("Enter the number to check if it is EVEN or ODD"))
# def check_num(num):
#     if num % 2 == 0:
#         print("EVEN") 
#     else:
#         print("ODD")
#     return num

# check_num(num)

"""RECURSION IN PYTHON"""
# when a function call itself repeatedly (same like loops)
#prints n to backward 
# def show(n):
#     if(n == 0): # base case : if not base case it becomes unlimitted loop
#         return
#     print(n)
#     show(n-1) #show function calling itself for new vales (n-1)
# show(4)

#return n!
# NO FACTORIAL FOR NEGATIVE NUMBERS
#recursive relationship n! = (n-1)! x n (Recurrence Relation)
# n = int(input("Enter number"))
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n* fact(n-1)     #fact(n) = fact(n-1)*n
# print (fact(n))

"""PRACTICE QUESTIONS"""
# Question 1: Write a recursive function to calculate the sum of first 3 natural numbers.

# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n
# print(calc_sum(5))

# Question 2: Write a recursive function to print all elements in a list.(use list & index as parameter)

# def p_list(list,idx  = 0):
#     if(idx == len(list)):
#         return 
#     print(list[idx])
#     return p_list(list, idx+1)
# list = [1,2,3,4,5]

# print(p_list(list, idx=0))