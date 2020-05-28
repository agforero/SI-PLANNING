




































# CLASS STUFF
# 1
class Polygon:
    def __init__(self, n): # the most important class function!!!
        self.sides = n     # remember: self is an argument in every class method.

    # 3
    def findAngles(self):
        return ((self.sides - 2) * 180) / self.sides

# 2
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

# 4
timmy = Triangle()
#print(timmy.findAngles())

squidward = Polygon(4) # a square
#print(squidward.findAngles())

# 5
def comparePoly(s1, s2):
    if s1.sides > s2.sides:
        return 1
    
    elif s1.sides < s2.sides:
        return 2

    else:
        return 0

#print(comparePoly(timmy,squidward)) # returns 2 because the second Polygon has more sides (a square).

'''
AND NOW A SPECIAL MESSAGE FROM YOUR GRACIOUS SI LEADER:

The basic syntax for class inheritance is the following:

class Parent:
    def __init__(self, A):
        self.thing = A

class Child(Parent):
    def __init__(self):
        Parent.__init__(self, S)

where the terms have the following meanings:

- Parent: the overarching class of which the Child is a part of. Like, Polygon.
- Child: the more specific class that inherits the properties of the Parent. Like a Triangle.
- A: the attribute (or attributes) of the Parent. For example, how many sides a Polygon has.
- S: the attribute (or attributes) that makes the Child special. In the case of the Triangle, 
  the fact that it always has 3 sides.

'''

# FILES AND LISTS
# 6
thomas = ("I'm Agustin, I'm", 20, "and I never learned how to f***ing read.")

# 7
lenny = ["Agustin", "Alexia", "Max", "Chloe"]

# 8 
lenny[2] = "Jerry Seinfeld"

# 9
#for i in range(len(lenny)):
#    print(lenny[i])

# 10
f = open("fPrep.txt", "r")
count = 0

for i in f:
    line = i.split() # splits each line up by spaces
    for j in line:
        if j == "the":
            count += 1

f.close()
#print(count)

# 11
name = "Agustin"
age = 20

#print("I'm Agustin, and I am %d years old!" % age )
#print("I'm %s, and I am %d years old!" % (name, age))
#print("You currently have %f dollars in the bank." % bal)

# 12 
def findD(s, n = 0):
    print(s)
    
    if len(s) == 0:
        print("No 'D' found!")
        return 0

    if s[0] == 'D':
        print(n)
        return n

    else:
        findD(s[1:], n+1)

#findD(['A','B','C','E'])

# 13
def tryExcept():
    try:
        print('a' + 3)

    except:
        print("YOU CAN'T ADD THOSE YOU DUMMY")

#tryExcept()

# 14

def xGTy(x, y):
    return (x > y)

def compare(x, y):
    if (xGTy(x, y)):
        print("Yep")

#compare(9,3)

# 15
#print((xGTy(9,3) and xGTy(3,9)) or not xGTy(9,9))

'''
(xGTy(9,3) and xGTy(3,9)) or not xGTy(9,9)
-------------------------

(xGTy(9,3) and xGTy(3,9))
 ---------
9 > 3 -> TRUE

(TRUE and xGTy(3,9))
          ---------
3 > 9 -> FALSE

(TRUE and FALSE)
----------------
FALSE

(FALSE) or not xGTy(9,9)
               ---------
9 > 9 -> FALSE

(FALSE) or not (FALSE)
           -----------
TRUE

(FALSE) or TRUE
---------------
TRUE
'''

# 16
print(lenny)
print(lenny.pop())