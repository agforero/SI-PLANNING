'''
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
- Now, let's look a bit at recursion.
- Recursion is super weird, and not entirely intuitive; from the time we're young, we're thought to think iteratively.

- Iteratively: in iterations. Step 1, then step 2, then step 3.
- Recursively: in itself. Step 1, then step 2 as a part of step 1, then step 3 as a part of step 2.

- Before we begin anything, remember the usage of colons in indexing. For example:

name = "Agustin"
print(name[1:]) -> "gustin"

series = [1, 2, 3, 4, 5]
print(series[1:]) -> [2, 3, 4, 5]
print(series[:3]) -> [1, 2, 3]

- First, let's start simple: define a recursive function that returns the location of the first letter 'a'. For example:

  findA("Giraffe") -> 3.
        0123

- Next, let's step things up a bit: given a list of lists, where each sub-list is a pair, write a recursive function
  that reverses the order of each sub-list. For example:

  invert([[1,2],[3,4],[5,6],[7,8]]) -> [[2,1],[4,3],[6,5],[8,7]]

- Now, try writing a recursive function that takes in three arguments:

  c1 and c2: two chars to be flipped, and 
  s: a list of chars to flip the characters in.

  This function will flip any instance of c1 with c2, and vice versa. For example:

  swapper('a', 'b', ['a', 'b', 'c', 'd', 'a']) -> ['b', 'a', 'c', 'd', 'b']

  It's okay to return a list of characters instead of a full string, if you like. Above, ['b', 'a', 'c', 'd'] is acceptable.

- Similarly, write a recursive function that takes in three arguments:

  c: a char to replace with,
  idx: the index location at which to place this new character, and 
  s: the list of chars to edit. This function will thus result with:

  listSet('a', 4, ['v','w','x','y','z']) -> ['v','w','x','y','a']
                                              0   1   2   3   4

  The challenge here is that we're only allowed three arguments instead of four. How might we get around this?

- Write a recursive function that skims through a list of numbers and removes any above 9. For example:

  skim([1, 4, 8, 12, 42, 5, 7]) -> [1, 4, 8, 5, 7]

  Use as many arguments as you like. You could also use a helper function if you'd like to.
'''
































def findA(str, n = 0):
    # safeguard
    if len(str) == 0:
        return "No instance of 'a' found."

    # stopper
    elif str[0] == 'a':
        print(n)
        return n

    # continuity
    else:
        findA(str[1:],n+1)

#print(findA("Apricots are delicious!"))
#           0123456789

def switch(ls):
    a = ls[0]
    b = ls[1]
    ls[0] = b
    ls[1] = a
    return [ls] # need square brackets to maintain structure

def invert(ls):
    # safeguard
    if len(ls) == 0:
        return []

    # continuity
    ls[0] = switch(ls[0])
    return ls[0] + invert(ls[1:])

#print(invert([[1, 2], [3, 4], [5, 6], [7, 8]]))

def swapper(c1, c2, s):
    print(s)
    # safeguard
    if len(s) == 0:
        return ''

    # swapping
    elif s[0] == c1:
        s[0] = c2
    elif s[0] == c2:
        s[0] = c1

    # continuity
    return s[0] + swapper(c1, c2, s[1:])

print(swapper('a', 'b', ['a', 'b', 'c', 'd']))

def listSet(c, idx, s):
    # safeguard
    if len(s) == 0:
        return ''

    # swapping
    elif idx == 0:
        s[0] = c
        return s

    # continuity
    return [s[0]] + listSet(c, idx-1, s[1:]) # had to enclose in square brackets here.

#print(listSet('a', 4, ['v','w','x','y','z','x']))

def remove(ls, idx):
    return ls[:idx] + ls[idx+1:]

#print(remove("Agustin", 1))

def skim(ls): 
    # safeguard
    if len(ls) == 0:
        return []

    # functionality
    if ls[0] > 9:
        return skim(ls[1:])
    
    # continuity
    return [ls[0]] + skim(ls[1:])

#print(skim([1, 4, 8, 12, 42, 5, 7]))