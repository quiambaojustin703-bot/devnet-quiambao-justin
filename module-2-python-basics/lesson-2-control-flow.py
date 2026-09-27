"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Justin Quiambao
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Hello, my friend! Today, I will explain to you what Control Flow is.
Control flow is used to make decisions in a program. 
It allows the program to check a condition and choose what code to run.
We can use if, elif, and else to make different choices depending on the situation.


============================================
KEY VOCABULARY
============================================
- condition: something that the program checks to make a decision.
- if / elif / else: statements used to choose which code will run.
- comparison operator: a symbol used to compare values, such as >, <, or ==.
- boolean expression: an expression that results in True or False.


============================================
MY OWN EXAMPLE(S)
============================================
"""

grade = 85

if grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I wrote grade = "85" with quotation marks, then i tried 
if grade >= 75:. I got a type error: "'>=' not supported between 
instances of 'str' and 'int'." This taught me that you can't use 
comparison operators like >= between a string and a number the 
data types need to match, so the value has to actually be an int 
for comparisons like this to work.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Control flow is used everywhere in real programs, like checking if 
a password is correct before logging in, or deciding what grade 
label to show a student based on their score. Any time a program 
needs to make a decision based on a condition, if/elif/else is 
what makes that possible.
"""
