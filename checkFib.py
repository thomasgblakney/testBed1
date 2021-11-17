# python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):

    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


# A utility function to test above functions
for i in range(1, 170):
    if isFibonacci(i) == True:
        print(i, "is a fibonacci Number")
    else:
        print(i, "is a not fibonacci Number ")
for i in range(1, 170):
    if isPerfectSquare(i) == True:
        print(i, "is a Perfect Square")
    else:
        print(i, "is not a Perfect Square")
# how can I make this print two columns?
