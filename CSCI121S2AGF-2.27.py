'''
-   Testing code?
-   If one thing causes an error in one place, it'll cause errors everywhere.

-   Make a Python function to find the max in a list. Generate the list using 

    import random

    ls = []
    for i in range(10):
        ls.append(random.randint(1,10))

    Define it findMax(). What argument(s) will you need?
-   Do the same thing, but find the minimum instead.
-   Write a function that checks if a number is prime. Plan out for a bit how 
    you'd do this, either by writing out an approach on the board or by talking
    it over with me or a partner.
-   Write a function to flip the sign of an integer. If the input is -9, have the 
    function return 9 instead.
-   Write a function to print out all Fibonacci numbers up to argument n.

'''

import random

ls = []
for i in range(10):
    ls.append(random.randint(1,25))

print(ls)

def findMax(ls):
    max = 0
    for i in ls:
        if i > max:
            max = i

    return max

def findPrime(n):
    for i in range(2,10):
        x = n % i
        if x == 0 and not x == i:
            return False
        else:
            return True

def findPrime2(n):
    x = 2
    for i in range(n-2):
        if n % x == 0:
            return False
    
    return True

def fib(n):
    x = 1
    y = 1
    sum = 0
    while (sum < n):
        sum = x + y
        x = y
        y = sum
    
    return sum

def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)

def main():
    print("Maximum:" , findMax(ls))
    print("29 is prime????? ", findPrime(29))
    print("123 is prime????? ", findPrime2(123))
    print("fib(200): ", fib(200))
    print(fact(10))

main()