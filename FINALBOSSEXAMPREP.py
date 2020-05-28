'''
ALRIGHT FELLAS, IT'S TIME TO REVIEW FOR THE FINAL!!!!!

Up to bat are a couple of concepts you guys have requested for me:

CLASS STUFF:
- Classes
- Class methods
- Inheritance

FILES AND LISTS:
- Lists vs. tuples
- Iterating through lists
- Importing files and reading them
- String formatting

MISC.:
- Recursion 
- Exceptions 
- Boolean values vs logical operators
- pop()
- CSS
'''

# CLASS STUFF
'''
1.
First, let's start by definining a class Polygon that takes in one argument in its
initiator: the total number of sides.

2.
Let's now create a subclass of Polygon called Triangle. This subclass inherits the 
initiator of its parent, but automatically assigns 3 to the number of sides.

3.
Now, create a method in the Polygon class that returns how many degrees will be 
found in an angle of that shape. Remember: the sum of all angles of a shape is 
(n - 2) * 180, where n is the total number of sides. 

4. 
Test the above function on a triangle, and a polygon of your choice.

5.
Now, write a function (NOT within one of the previous classes) that compares two 
Polygons and finds if the first or second Polygon has more sides. 

Return:
- 1 if the first Polygon has more sides, 
- 2 if the second Polygon has more sides, and
- 0 if the Polygons have the same number of sides.

Test this function on the shapes you made for question 4, and print the result.
'''

# FILES AND LISTS
'''
6.
There are three big differences between lists and tuples:

- Lists are homogeneous, tuples are heterogeneous.
- Lists can be edited, tuples cannot.
- Lists use square brackets, tuples use parentheses.

Define a tuple, putting in elements of several different types. Do what you want, homie.

7.
Define a list of 4 names.

8. 
Change the third name in the list to be something else.

9.
Print all of the elements in the list. 

10. 
Now, onto file reading: remember, once you've opened a file for reading, it basically just
becomes a glorified list.

Open the file "fPrep.txt" and find how many "the"s are present. Close the file afterwards.

11. 
Use string formatting to print your age in the middle of a string about yourself. For example:

age = 20
"I'm Agustin, and I am 20 years old!"

Remember, string formatting is when we take print() and add extra elements using the percentage 
symbol (%). The following are a list of relevant symbols:

- %s: a string
- %d: an integer (don't ask me why it's d instead of i, I have no idea)
- %f: a float.

Fun fact: these are actually the same symbols as C.
'''

# MISC.:
'''
12. 
Recursion: write a recursive function that takes in a string and prints the location of the first uppercase 'D'.
For example: findD(['A','B','C','D']) -> 3

13.
Make a try/except statement that attempts to add together a character and a number. Print a polite error message
for when this inevitably doesn't work out.

14. 
Booleans are TRUE/FALSE values that change depending on a set of conditions. For example:
'''

def xGTy(x, y):
    return (x > y)

'''
xGTy() will return certrain Booleans depending on the following values of x and y:

- (9, 3) -> TRUE
- (3, 9) -> FALSE
- (9, 9) -> FALSE 

Using the xGTy() function above, define another function that prints "Yep" if x is greater than y.

15. 
A logical operator is a term we use to link multiple booleans together. This includes three cases:

- and (BOTH elements must be true)
- or (AT LEAST ONE element must be true; they aren't mutually exclusive)
- not (the opposite of the boolean in question).

For and, a Boolean table for the following T/F values would look like this:

        T   F

T       T   F
F       F   F   <- this last element in the table is the equivalent of (FALSE and FALSE), which evaluates to FALSE.

For or, the table would look like this:

        T   F

T       T   T
F       T   F   <- this last element in the table is the equivalent of (FALSE or FALSE), which also evaluates to FALSE.

not is different from and, as well as or; all it does is give the opposite of the boolean in question.

- not TRUE -> FALSE
- not FALSE -> TRUE

Going back to the example from before, the following lines would give these outputs:

- not xGTy(9, 3) -> not TRUE -> FALSE
- not xGTy(3, 9) -> not FALSE -> TRUE
- not xGTy(9, 9) -> not FALSE -> TRUE

With all of this in mind, what would be the value of:

(xGTy(9,3) and xGTy(3,9)) or not xGTy(9,9)?

16.
Remember that list of names from earlier? Use pop() to shave off the last value, then 
print the result.

'''