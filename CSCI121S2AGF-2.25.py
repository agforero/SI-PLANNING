'''
-   Accumulators
-   Assigning variables the return of functions
-   Difference between arguments and parameters
-   Accumulators in arithmetic sums
-   Importing stuff (have to be in the same folder)
-   Combining accumulator stuff with turtles
-   Using accumulators to have repetitive functions increase in scope

    Exercises:
-   Write a function that converts parameter n to either Celsius or 
    Fahrenheit. Ask the user which type they are converting to.
-   Write a function fact(n) that calculates the factorial of n. Write out
    or discuss a plan for 5 minutes, then implement it in IDLE.
-   Write a function lumber() that computes how many times you'd have to
    multiply 2 by itself to get at least n. Write/discuss it for 5, then
    implement. What mathematical function is similar to this?
-   Rewrite the same function, but instead of powers of 2, have it as a 
    user-defined n. Call it lumber2().
-   Write a function search() that takes in two arguments:
    -   ls: a list of integers, and
    -   n: a number to search for
    The function will then search through the list and find how many 
    occurrences of n there are. It then returns this value. Write/discuss 
    for 5, then implement. Generate a list of 50 random numbers to use.
-   Do the same thing, but return a list of all indices where that n can
    be found. Call it search2().
'''


import random

ls = []
for i in range(10):
    ls.append(random.randint(1,10))

print(ls)


def convert(n):
    ans = input("Would you like to convert to Celsius or Fahrenheit? C/F ")

    if ans == 'C':
        return (n-32) * (5/9)
    else:
        return (n * (9/5)) + 32

def fact(n):
    for i in range(n):
        n *= (i+1)

    return n

def lumber(n):
    x = 2
    count = 0
    while (x < n):
        x *= 2
        count += 1

    return count + 1

def lumber2(n, x):
    x = x
    count = 0
    while (x < n):
        x *= x
        count += 1

    return count + 1

def search(ls, n):
    count = 0
    for i in ls:
        if i == n:
            count += 1

    return count

def search2(ls, n):
    inds = []
    for i in range(len(ls)):
        if ls[i] == n:
            inds.append(i)

    return inds

def main():
    # temp = convert(50)
    # print("Your converted temperature is: ", temp)

    # print("The factorial of 10 is", fact(10))
    # print("2 needs to be multiplied by itself", lumber(100), "times to be at least 100.")
    # print("3 needs to be multiplied by itself", lumber2(100,3), "times to be at least 100.")

    print(search(ls,1))
    print("1 is found at indices:", search2(ls,1))
    
main()