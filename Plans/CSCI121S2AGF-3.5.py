'''
While loops. Finally.

1.  Write a function to print the square of all numbers from 0 to 10.
2.  Write a function to print the sum of all EVEN numbers from 0 to 100.
3.  Write a function to read in three numbers a, b and c, and check
    how many numbers between a and b are divisible by c.
4.  Write a function that prints the following output:

    1 99
    2 98
    3 97
    ...
    97 3
    98 2
    99 1

    How would you do this with a while loop? How would you do this 
    with a for loop?
5.  Write a function that prints a right triangle using asterisks. 
    For example: 

    fn(5) -->

    *
    **
    ***
    ****
    *****

6.  Write a function that prints all prime numbers between 0 and n.
    Have the function then return the number of numbers found.
7.  Given three single-digit numbers a, b and c, write a function 
    that prints all permutations of the three. (Next time)
'''
def p1():
    for i in range(11):
        print(i**2)

    n = 0
    while (n < 11):
        print(n**2)
        n += 1

def sumTo(n):
    i = 0
    counter = 0
    while i <= n:
        counter += i
        i += 2
    return counter

def p2(n):
    count = 0
    for i in range(int((n+2)/2)):
        count += i*2

    return count

def p3(a,b,c):
    count = 0
    for i in range(a,b+1):
        if i % c == 0:
            count += 1

    return count

def p4():
    x = 1
    y = 99
    while x < 100:
        print(x,y)
        x += 1
        y -= 1

def p5(n):
    count = 1
    str = "*"
    while (count <= n):
        print(str)
        str += "*"
        count += 1

def p5Broken(n):
    count = 1
    str = "*"
    while (count <= n):
        print(str)
        str += "*"

def prime(n):
    count = 0
    for i in range(2, n-1):
        if n % i == 0:
            count += 1 # counts times a number can be divided into n
    if count > 0:
        return False
    else:
        return True

def p6(n):
    count = 0
    for i in range(n+1):
        if prime(i):
            print(i)
            count += 1
    
    return count

def cPrime(n):
    counter = 0
    for i in range(2,10):
        while n >= 1:
            r = n % i
            if r != 0:
                counter += 1
                print(n)
            n -= 1
    
    return counter

def main():
    #p1()
    #print(sumTo(10))
    #print(p2(10))
    #print(p3(1,50,5))
    #p4()
    #p5(10)
    print("Total prime numbers up to 100:", p6(100))
    #print("Total prime numbers up to 100:", cPrime(100))    

if __name__ == "__main__":
    main()