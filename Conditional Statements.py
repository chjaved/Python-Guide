# CONDITIONAL STATEMENTS
# IF-ELIF-ELSE
# Structure
# if(condition1):
#     statement
# elif(condition2):
#     statement
# else
#     statementN

# age = int(input("enter age:"))

# if(age >= 18):
#     print("can vote & apply for license") #indentation
# elif(age <= 18):
#     print("cannot vote and apply for license")
# else:
#     print("invalid input")

# #Grade students based on marks
# marks = int(input("enter marks to check grade"))

# if(marks >=90):
#     print("GRADE A")
# elif(marks >=80 and marks <90):
#     print("GRADE B")
# elif(marks >= 70 and marks<80):
#     print("GRADE C")
# else:
#     print("GRADE D")

# Practice Questions

# Write a program to check if a number is entered by the user is odd or even.
# num = int(input("Enter the number:"))
# print(num)
# if(num%2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")

#Write a program to find the greatest of 3 numbers entered by the user
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))

# if(num1 > num2 and num1 > num3):
#     print(num1," is greater")
# elif(num2 > num3 and num2 > num1):
#     print(num2, "is greater")
# else:
#     print(num3, "is greater")

# Write a program if a number is multiple of 7 or not.
num = int(input("enter the number"))
if(num%7 == 0):
    print(num,"is dvisible of 7")
else:
    print(num,"not divisible of 7")