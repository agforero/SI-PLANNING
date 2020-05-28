'''
-   Boolean stuff
-   Comparators
-   Boolean operators
-   and 
-   or
-   not?
-   Logical opposites. Brain hurty
-   Literally just Formal Logic
-   Logic table?? Something like:

    Case 1: a = 0, b = 0
    Case 2: a = 0, b = 2            
                                    C1Eval  C2Eval
    Cond 1: a == 0 and b > 1        True    False
    Cond 2: a != 0 or  b <= 1       False   True

    Oh god this makes my brain hurt
-   Using Booleans to determine if a number is odd.

-   Make a function to check if first value n1 is greater than second value n2.
-   What is the logical opposite of:
    a == 0
    b < 5
    c >= 7

-   How about the logical opposite of:
    a == 5 and b <= 2
    a < 5 or b >=0

-   You're going on a vacation (to where, I don't know...decide for yourself, okay?)
    You start your vacation on a Friday. Based on the number of days you plan to
    be gone, write a function that computes whether or not you'll return on a Friday.

-   Write a function that will take in a float and round it down to the previous whole
    number. For example, 3.75 becomes 3 when plugged in.

-   Write a function that computes the length of a hypotenuse, given a right triangle
    with sides a and b. What library might you need to import?

-   Write a function isRightAngled(a,b,c) that computes if a triangle with the given
    sides is a right triangle. Assume c is the hypotenuse. The function from before
    might prove handy.

'''
import math 

def checkGreater(n1, n2):
    return n1 > n2

def checkFriday(days):
    n = days % 7
    return n == 0

def roundDown(f):
    return f // 1

def roundLegit(f):
    if f % 1 < 0.5:
        return f // 1
    else:
        return (f // 1) + 1

def hypot(a,b):
    return math.sqrt(a**2+b**2)

def isRightAngled(a,b,c):
    return (c**2) == (a**2+b**2)

def main():
    print(checkGreater(4,3))
    print(checkFriday(134))
    print(roundDown(3.984))
    print(roundLegit(3.2),roundLegit(9.9))
    print(hypot(3,4))
    print(isRightAngled(3,4,5))

if __name__ == "__main__":
    main()  