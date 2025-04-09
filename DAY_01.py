""". Variables & Data Types

    Swap Two Variables

        Take two variables a = 5 and b = 10, swap their values without a third variable."""
"""
a=10
b=20
a , b= b,a
print(a,b)
"""

""""Convert Temperature

        Convert Celsius to Fahrenheit: F = (C × 9/5) + 32 (Take C = 37)."""
"""
c=int(input("enter your number : "))
F = (c * 9 / 5) + 32

print(F) """

"""Calculate Area of a Circle

        Given radius = 7, compute area using Area = πr²."""

"""r=int(input("enter your radius number : "))

area=3.14 * r*r

print(round(area))"""

"""2. Conditional Statements (if-elif-else)

    Check Even or Odd

        Take a number n = 13, print if it’s even or odd."""
"""
n=int(input("enter a number : "))
if n%2==0:
    print("{}is even number".format(n))
    #print(f"{n }is even number")

else:
    print(f"{n} is odd number ")"""

"""  Find the Largest Number

        Given three numbers a = 5, b = 10, c = 7, print the largest one."""

"""a = 5
b = 10
c = 7

lar = a if (a>b and a>c) else (b if b>c  else c)
print(lar)"""