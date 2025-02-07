
#2 - Variables
#strings cannot be used for math, only integers (without quote marks)
#strings + integers = TypeError

"""FOUR BASIC DATA TYPES"""
#Strings = letters
#Integers = whole numbers
#Float = numeric value that have decimals
#Boolean = True or False

print("string") #or Print(variable)  = Prints into console
##print(type("something"))            = returns STRing/INTeger/FLOAT/BOOL
#print(variable1+" "+variable2)   = " " adds a space between the variables

#str(var)    = changes the "var"iable into a string to avoid TypeError
#    \__ called as typecasting
#---------------------------------------------------------------------------

#height = 250.5
#print("Your height is: "+str(height)+"cm")
#print(type(height))

#---------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#--------------------------------------------------------------------------

#3 - Multiple Assignment
#multiple assignment = allows us to assign multiple variables at the same time in ONE line of code

#---------------------------------------------------------------------------

#Use
#name, age, attractive = "Bro", 21, True

#instead of
#name = "Bro"
#age = 21
#attractive = True

---------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
---------------------------------------------------------------------------

#4
"""len(name)            = returns how long the string is
name.find("o")       = finds a character within a string (starts at 0)
name.captialize()    = capitalizes the first letter in the string
name.upper() = makes string ALL uppercase
name.lower() = makes string ALL lowercase
name.isdigit()   = returns True or False if string is a digit/integer
name.isalpha()   = if string is ALL alphabetical letters (no spaces)
name.count("o")  = counts how many characters i.e how many "o"
name.replace("o","a")    = replaces all "o" characters with "a"
name*3   = displays name THREE times (without spaces)
name.center('x', "y") = length in character count(x) and empty space(y)
name.swapcase() = changes lowercase to uppercase and vice versa
name.title() = makes every first letter in every word uppercase (titlecase)
"""
#---------------------------------------------------------------------------
"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
#---------------------------------------------------------------------------

#5 - Type Casting
#type casting = convert the data type of a value to another data type

#---------------------------------------------------------------------------

"""x = 1       #int
y = 2.0     #float
z = "3"     #str

x = float(x)
y = int(y)
z = int(z)

print(x)
print(y)
print(z*3)"""#

#RETURNS

#1.0     #x
#2       #y
#9      #z*3
#---------------------------------------------------------------------------

#6 - User Input
#input()

#---------------------------------------------------------------------------

#name = input("What is your name?: ")
#age = int(input("How old are you?: "))     = [must only be a whole number]
#height = float(input("How tall are you?: "))

#age = age + 1       = [Needs int typecasting to calculate]

#print("Hello "+(name))              = [doesn't need typecasting when a string]
#print("You are "+str(age)+" years old") = [returns int(age) into str(age) print]
#print("You are "+str(height)" cm tall")

#---------------------------------------------------------------------------
""""""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
---------------------------------------------------------------------------

#7 - Math Functions
# these functions are located in the math module
# always use "import math" before using math module codes

---------------------------------------------------------------------------



pi = -3.14

round(pi) -> -3                   =round off
    value.__round__(x)          = round off float(?)
math.ceil(pi) -> -4              =ceiling
math.floor(pi) -> -3            =floor
abs(pi) -> 3.14                    =absolute value
pow(pi,2) -> 9.8596            = value ^ raised to power of, "value"
math.sqrt(420) -> 20.49     =square root

x = 1
y = 2
z = 3

max(x,y,z)  -> 3   = finds the maximum value between a set of values
min(x,y,z) -> 1     = finds the minimum value between a set of values"""
#9 - IF STATEMENTS 
# if statement = a block of code that will execute if it's condition is true
"""if:
else:
elif:

= assignment property
== comparative/comparison property
---------------------------------------------------------------------------

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 100:
    print("You are older than a century!")
elif age >= 18 and age <= 99:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

---------------------------------------------------------------------------
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
---------------------------------------------------------------------------

#10 - LOGICAL OPERATORS
# logical operators (and, or, not) = used to check if two or more conditional statements are true
#and
#or
#not()

---------------------------------------------------------------------------

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
if temp < 0 or temp > 30:
    print("the tempperature is bad today!")
    print("stay inside!")

OR

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("the tempperature is bad today!")
    print("stay inside!")
if not(temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outside!")"""

#validate user input exercise
username=input("enter the username:")
if len(username)>12:
    print("put username less than 12")
elif not username.find(" ")==-1:
    print("no space plz")
elif not username.isalpha():
    print("dont enter digits")
else:
    print(f"welcome {username}")