'''
Function stuff.
What are the differences between the mathematical notion of a "function" 
and the Python notion of a "function"? Something like:
f(x) = 2x + 3 versus defining the same thing in Python.

The students said:
-   There's an input, and an output. The notion by which you represent each is
    different between the two.
-   Mathematics are timeless. In a programming language, however, we need to
    worry about sequencing.
-   In Python, you can accomplish more complicated functions, or at least in
    a more legible fashion.

He then went over the syntax of a Python function definition.
'''
#     v parameter
def f(x):
    return (2*x) + 3

print(f(2) + f(3))
#       ^      ^ arguments
'''
Exploring the difference between the two.
A student asked if it was possible to declare new variables within the 
body of a function. Olaf responded with yes, you can do whatever you want
in the body, which makes functions incredibly useful and adaptive.

A huge part of today was the return function. What it does, what it means,
what happens if you return nothing. For example, one student asked: "If 
you return 'None', are you returning a string, or null, or what?"

There's also the idea of localization. What variables are accessible, and
when? "Amnesia" in forgetting things we've made in functions. What kind 
of variable is returned with return statements? Why do some functions
return None?

Function calls are kinda like variables. They have assigned values, as per
their return statements. How can I illustrate this?

Maybe this Sunday I can show them how to install VSCode? Alongside the 
necessary extensions, and how to run the Python program.
'''

'''
Let's program a dog. The dog will be a list with whichever date we want
to attribute to them: 

dog = [name, species, gender, coat, age, # of limbs, size, price...]

We will update different parts of this list with functions. We can also
add more attributes later by increasing the size of the list.

Let's start by making a function to create our dog. The function will have
0 arguments; instead, the function itself will ask the user to define each
of the different data points of our dog.

Next, let's try making functions that...

1.  Rename our dog.
2.  Redefine what species of dog they are.
3.  Asks for their gender.
4.  Change the color coat they have.
5.  Asks their age.
6.  Adds or subtracts limbs from the dog. Maybe the dog was born in 
    Chernobyl or something.
7.  Increases or decreases the size of the dog. We can measure the 
    size of the dog with pounds, inches of height, etc.
8.  Increases or decreases the price of the dog.
9.  Makes the dog bark. Print the name of the dog followed by a "bark!"

Now, let's sell our dog. We want a function that takes in one argument: the
money the user has. Print out all the attributes of the dog at this point; 
the user should know what they're paying for. If the user doesn't have 
enough money to buy the dog, tell them in a friendly print statement; other-
wise, congratulate them on their new purchase of <dogname>.
'''