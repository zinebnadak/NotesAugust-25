# a variable is when a name is used to store value for later use in program:
a=42
print(a)

# type of a=123 is an integer, BUT b="123" is a string
a=123
b="123"

print(type(a))
print(type(b))

# multiple assignment: name multiple variables simultaniously
v,s=5,"hello"

print(v)
print(s)


#Program that reads and writes. Input argument, use end=" to keep in line
name =  input ("what is your name?")
print("Hello", name,"!", end="")
age = input(" How old are you?")
print("Your name is", name,",and you are", age, "years old")

#Program that reads and calculates. Gives me the integer number squared. OBS! ONLY Integer number work!
answer = input ("write me a number:")
x=int(answer)
y=x*x
print ("The square of the number", answer, "is",y)

# if you want the program to be able to print both integer and float numbers use float
answer = input ("write me a number:")
x=float(answer)
y=x*x
print ("The square of the number", answer, "is",y)

#use formated string litterals, called f-strings to get the calculated float number neater ex. 1.6. For these we use curly braces/placeholders {}."y" = what is going to be answered. After ":" comes a formatspecification telling us how it is going to be answered. Follow up with a dot "." ,then "2", means answer with two decimals. Lastly "f" stands for float number. Use d for Integer numbers or nothing at all.
answer= input("write a number")
x=float(answer)
y=x*x
print(f"The square of the number is {y:.2f}")

#you can also replace {y:.2f} to {x*x:.2f} directly and skip a line for shorter code

#adding a number before the dot tells you how many big the spaces is going to be printed in the answer
print(f"The square of the number is {y:6.2f}")
# program gives you 6 spaced of which only 4 are used to print numbers
print(f"The square of the number is {y:06.2f}")
# program gives number starting with 0 to fill up the given space

#you can use multiple placeholders in one single f-sting
i=3
j=6
print(f'i={i} and j={j}')

#adding "=" after variable to
print (f'{i=} and {j=}')


#another way to write calculation program with expression and formatspecifications, OBS! INPUT FUNCTIONS ALWAYS RETURNS A STRING EVEN IF USER INPUTS A NUMBER
x= float(input ("give me a number"))
print(f"{x * x:.2f}")

#arithmetic expressions = expressions resulting  a numerical value ex. 1+2 or 6/3. + and - are called numerical operations, while 1 and 2 är numerical operands.
# An expression has a worth and a type

# Here is a simple program that calculates a squares side. The program calculates perimeter and area!
#user input
#calculate perimeter
#calculate area
#print answer

#LESSON NOTES
#Exercise using the "math" module, which is not built in like ex. abs() or round():Cosine of 1, Cosine of pi, Cosine of 45 degrees (convert degrees to radians using an appropriate function, consult the documentation!), The square root of the cosine of 45 degrees

#get empty line
print ("Hello World!")
print ()
print ("that is how you get an empty line")

import math
#ex1
print(math.pi)

#ex2
print(math.sqrt(81))

#ex3
print(math.sin(math.pi))

#ex4
x=45
math.radians(x)
result = math.cos(x)
print(result)
#obs you need to store the value of x (now in "result") for it to used the calculated version and not the firt given
# for shorter code use multiple parenthesis
print(math.cos(math.radians(45)))

#ex5
print(math.sqrt(math.cos(math.radians(45))))

from math import pi, sqrt, cos, radians #lets you use these without repeating math in your code and use "result" to print result

result = sqrt(cos(radians(45)))
print(result)

#specify strings using "str"":print ("Hello"+123) gives you error, compare:
print ("Hello"+" 123")
print ("Hello","123")
print ("Hello" ,str (123))
#all these work, look up "PEP 8's style guide" for string quotes in PEP (The Python Enhancement Proposal (PEP) related to advanced string handling, particularly for creating reusable and structured text)

#// gives us exact value of a calculation
a=7
b=3
print(a//b)

# % give us the remainder after division
a=10
b=3
print(a%b)
# answer gives us 1 because 3 goes exactly 3 times in 10 and rest is 1
