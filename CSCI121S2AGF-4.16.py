'''
Now we're officially getting into lists, which is pretty nifty.
We're also getting into reading files.

- Make a list including your name and the names of two of your friends. Then,
print out the third name in the list.

- Write a function that, given the input.txt file I sent you, finds all instances
of "A" and prints out its line and column indeces in the file.

- Given the completely insigificant file bee.txt, write a function that 
finds all instances of the word "bee" and returns the count of them.

- Build upon the previous function. Make a new function with the same body 
of code, only this time, the function returns a list of all locations of 
the "bee"s that it finds. For example, if line 4, word 2 is "bee", then [3, 1]
will be appended to the list. The return might look something like:

[[3,1],[6,7],[12,2],[14,3]...]

- Use this list to write all locations of "bee" to a new file, 
"locations.txt". If you don't know how to do this, we'll walk through it 
together. Put each individual location on its own line.
'''

def findA(filename):
    readfile = open(filename, "r")
    #line = readfile.split()
    linecount = 0
    lettercount = 0

    for line in readfile:
        letter = line.split()
        for i in letter:
            if i == "A":
                print(linecount, lettercount)
            lettercount += 1
        lettercount = 0
        linecount += 1
    readfile.close()


findA("input.txt")











def example1():
    f = open("input.txt")
    count1 = 0
    count2 = 0
    for line in f:
        ls = line.split()
        for i in ls:
            if i == 'A':
                print(count1, count2)
            count2 += 1
        count1 += 1 
        count2 = 0
    f.close()

#example1()

def example2():
    g = open("bee.txt")
    count3 = 0
    for line in g:
        ls = line.split()
        for i in ls:
            if i == "bee" or i == "Bee":
                count3 += 1
    print(count3)
    g.close()

#example2()

def example3():
    h = open("bee.txt")
    ls = []
    count1 = 0
    count2 = 0
    for line in h:
        temp = line.split()
        for i in temp:
            if i == "bee":
                temp2 = []
                temp2.append(count1)
                temp2.append(count2)
                ls.append(temp2)
            count2 += 1
        count1 += 1
        count2 = 0 # resetting word count
    h.close()
    return ls

#ls = example3()
#print(ls)

def example4(ls):
    k = open("locations.txt", 'w')
    for i in ls:
        k.write(str(i))
        k.write('\n')
    k.close()

#example4(ls)