'''
oh god, OOP

__init__ as a constructor, I think.
self refers to the object itself

RuneStone 17.7
'''

class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def printInfo(self):
        print(self.name, self.age)

    def addToAge(self, n):
        self.age += n

p1 = Human("Jeff", 18)
p1.printInfo()

p1.addToAge(10)
p1.printInfo()

hList = []
for i in range(10):
    hList.append(Human("test", i))

for i in range(10):
    hList[i].printInfo()

'''
- Define a class Dog with 5 attributes. Two of them should be:
    - name
    - age

  You will come up with the next three attributes.

- Make three functions within Dog to change the states of the attributes. For example:
'''

#def Dog:
    #def addAge(self, n):
    #    self.age += n

'''
- Now, let's make a class Shop. The Shop class will have three attributes: three different Dogs.
- After defining this class and the Dog attributes it holds, define a function within the Shop class
  that prints out the available Dogs, and asks the user to pick one. 

- Let's recreate the Pixel class.
- Make an initializer that takes in the red, blue and green values of the pixel.
- Make functions that set the red, blue and green values to be something new.
- Make functions that get the red, blue and green values.
- Make a function that neatly displays the pixel, eg: [100, 70, 90]
- Now, make a separate function that computes the average values of two pixels and assigns those averages to a new pixel.
- How might we shorten this function to be only two or three lines? You can make a helper function to assist you here.

- Answer seen below.
'''


















# def average(x, y):
#     return ((x+y)/2)

# def averagePixel(Pixel p1, Pixel p2):
#     Pixel p3(average(p1.getRed(), p2.getRed()), average(p1.getBlue(), p2.getBlue()), average(p1.getGreen(), p2.getGreen()))
#     return p3

'''
- Display the pixel we just created.
- Write a function that takes in a pixel as input, and returns a greyscaled version of the pixel as output.
'''