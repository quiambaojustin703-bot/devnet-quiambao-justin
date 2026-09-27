"""
Module 2 — Lesson 4: Functions
Student: Justin Quiambao
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC?
============================================
A function is a block of code used to perform a specific task.
It helps us reuse code instead of writing the same code again.
A function can receive a value and return a result.

============================================
KEY VOCABULARY
============================================
- function: a block of code that performs a task.
- Parameter: a variable that receives a value in a function.
- Argument: the actual value given to a parameter.
- Return: sends a result back from the function.


============================================
MY OWN EXAMPLE(S)
============================================
"""

def greet(name):
    return "Hello, " + name

name = greet("Justin")

print(name) 


"""
============================================
A MISTAKE I MADE
============================================
One mistake I want to avoid is a getting confused between a parameter
and an argument. I learn that the parameter is use when creating the function, while the argument is the actual value given when
calling the function.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This can also be connected to other programs. 
For example, if we want to create a calculator, functions can make the code shorter and easier to organize because we can reuse them for different values.
