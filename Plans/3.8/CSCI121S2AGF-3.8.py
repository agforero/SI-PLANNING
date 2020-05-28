'''
-   Escape characters: \t, \n, stuff like that
-   Nested for loops
-   end= (a thing I've never seen before), something that allows you to force Python to end a string with something other than \n. For example,

    print("Thingy", end="END") 
    print("Hello") will print
    ThingyENDHello

    i = 0
    while i < 3:
        print(i, end=' ')
    print()

    This will print:

    0 0 0 0 0 0 0 0 0 0 0 0 0 0 ...
-   cImage, oh boy!
-   day_13_image_starter_code.py would be helpful if it's available online.
-   Make a function that finds the majority color in an image between the r,
    g and b values.
-   Write a function that converts an image to greyscale.
-   Write a function that changes every other pixel to be completely bright
    red, blue or green depending on the user input.
-   Write a function that increases the saturation of the image. Write another
    one that does the opposite.
-   Write a function that finds the majority color in each pixel, and deletes
    the other two colors present. So, for example,

    f(10,200,20) -> (0, 200, 0)

'''

from cImage import *

def findMajority(img):
    rSum = 0
    gSum = 0
    bSum = 0
    
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            v = img.getPixel(col,row)
            rSum += v.red
            gSum += v.green
            bSum += v.blue

    if rSum > gSum and rSum > bSum:
        print("This image is majority red. The sum was", rSum)
        return rSum

    elif gSum > rSum and gSum > bSum:
        print("This image is majority green. The sum was", gSum)
        return rSum

    elif bSum > gSum and bSum > rSum:
        print("This image is majority blue. The sum was", bSum)
        return rSum

def makeGrey(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            v = img.getPixel(col,row)
            average = int((v.red + v.green + v.blue) / 3)
            v.red = average
            v.blue = average
            v.green = average
            img.setPixel(col,row,v)

def majorityKick(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            v = img.getPixel(col,row)
            if v.red > v.green and v.red > v.blue:
                v.green = 0
                v.blue = 0
            elif v.green > v.red and v.green > v.blue:
                v.red = 0
                v.blue = 0
            elif v.blue > v.red and v.blue > v.green:
                v.red = 0
                v.green = 0
            img.setPixel(col,row,v)
            
    
def main():
    win = ImageWin("My Window", 1200, 800)
    oImage = FileImage('cat.gif')
    oImage.draw(win)

    myImage1 = oImage.copy()
    myImage1.setPosition(myImage1.getWidth()+10, 0)
    makeGrey(myImage1)
    myImage1.draw(win)

    myImage2 = oImage.copy()
    myImage2.setPosition((myImage1.getWidth()*2)+20, 0)
    majorityKick(myImage2)
    myImage2.draw(win)
    
    findMajority(oImage)

    win.exitOnClick()

if __name__ == '__main__':
    main()

























