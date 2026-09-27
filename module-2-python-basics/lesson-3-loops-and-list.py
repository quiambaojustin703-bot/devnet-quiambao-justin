"""
Module 2 — Lesson 3: Loops & Lists
Student: Justin Quiambao
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Hello, my friend! Today, I will explain to you what Loops & Lists are. 
A list is used to store multiple values in one variable. 
A loop allows us to repeat a block of code without writing the same code many times. 
For example, we can use a for loop to go through each item in a list.


============================================
KEY VOCABULARY
============================================
- list: a collection of multiple values stored in one variable.
- for loop: repeats code for each item in a list or sequence.
- while loop: repeats code while a condition is True.
- index: the position of an item in a list.
- iteration: one repetition of a loop.


============================================
MY OWN EXAMPLE(S)
============================================
"""

subjects = ["Python", "Networking", "Database", "Web Development"]

for subject in subjects:
    print(subject)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I forgot to indent the print(subject) line inside my for loop. When 
I ran it, I got an IndentationError: "expected an indented block 
after 'for' statement on line 3." This taught me that Python uses 
indentation to know which lines of code belong inside a loop 
without it, Python doesn't know what to repeat.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Loops and lists are used everywhere in real programs for example, 
printing a list of students in a class, checking attendance for 
each student one by one, or calculating grades for multiple records 
without writing the same code over and over.
"""
