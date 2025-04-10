#
# 2. Problems on Conditional Statements (if-elif-else)
#
#     Check Positive/Negative: Determine if a number is positive, negative, or zero.
#
# n=int(input("enter a number: "))
# if n>=0:
#     print(f"{n} is postive number" )
# else:
#     print(f"{n} is negative number ")

#     Leap Year Check: Check if a year is a leap year.
#
# year=int(input("enter a year number is : "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")


#     Largest of Three: Find the largest among three numbers.
#
# a=10
# b=4
# c=5
#
# res= a if (a>b and a>c) else (b if b>c  else c)
# print(f"{res } is largest number ")


#     Vowel Checker: Check if a character is a vowel or consonant.
#
# vwl_ch=input("enter ur vowel char: ")
# vowel="a,e,i,o,u"
#
# if vwl_ch == vowel:
#     print(f"{vowel} is there in our input ")
# else:
#     print(f"{vowel} is not there input ",vwl_ch)

#     Password Check: Verify if a password matches a stored value.
#

# password=input("enter your password is : ")
# password1="mahesh"
# if password1 == password:
#     print(f"{password1} is same value password  {password}")
# else:
#     print(f"{password1} is not same {password}")
#     Grade Calculator: Assign grades (A, B, C, etc.) based on marks (0-100).
#
# marks=int(input("enter your marks : "))
#
# if marks>=91 and marks <=100:
#     print(f"{marks} grade is A")
# elif marks>=80 and marks<=90:
#     print(f"{marks} grade is B")
# elif marks>=71 and marks<=79:
#     print(f"{marks} grade is C")
# elif marks>=60 and marks<=79:
#     print(f"{marks} grade is D")
# else:
#     print(f"{marks} grade is not there")



#     Triangle Type: Check if three sides can form a triangle (and if it’s equilateral, isosceles, or scalene).
#
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
#
#
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("The sides can form a triangle.")
#
#     # Check the type
#     if a == b == c:
#         print("It's an Equilateral triangle.")
#     elif a == b or b == c or a == c:
#         print("It's an Isosceles triangle.")
#     else:
#         print("It's a Scalene triangle.")
# else:
#     print("The sides CANNOT form a triangle.")


#     Discount Calculator: Apply a 10% discount if the purchase amount is above ₹1000.
#
#     Odd/Even Sum: Given two numbers, print the sum if both are even, else print their product.
#

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# if a % 2 == 0 and b % 2 == 0:
#     print("Both numbers are even.")
#     print("Sum:", a + b)
# else:
#     print("At least one number is odd.")
#     print("Product:", a * b)


#     Age Classifier: Classify a person's age group (child, teen, adult, senior).

# age=int(input("enter your age : "))
# if age<=5:
#     print(f"{age} is child")
# elif age<=13:
#     print(f"{age} is teen")
# elif age<=18:
#     print(f"{age} is adult")
# else:
#     print(f"{age} is senior")