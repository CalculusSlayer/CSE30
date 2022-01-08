# -------------------------------------------------------------------------------
#  BinaryConversion.py
# -------------------------------------------------------------------------------

def printBinary1(n):
    """Prints the binary digits of n, in wrong order"""
    while n > 0:
        print(n % 2, sep='', end='')
        n = n//2
    # end
# end


def printBinary2(n):
    """Prints the binary digits of n, in correct order"""
    L = []
    while n > 0:
        L.append(n % 2)
        n = n//2
    # end
    L.reverse()
    for digit in L:
        print(digit, sep='', end='')
    # end
# end


def printBinary3(n):
    """Recursively prints the binary digits of n, in wrong order"""
    if n > 0:
        print(n % 2, sep='', end='')
        printBinary3(n//2)
    # end
# end


def printBinary4(n):
    """Recursively prints the binary digits of n, in correct order"""
    if n > 0:
        printBinary4(n//2)
        print(n % 2, sep='', end='')
    # end
# end


# ------------------------------------------------------------------------------
if __name__ == '__main__':

    #x = 2347
    x = 11
    #x = 0

    print()
    printBinary1(x)  # right to left
    print()
    printBinary2(x)  # left to right
    print()
    printBinary3(x)  # right to left
    print()
    printBinary4(x)  # left to right
    print()

    print()
# end

"""
Exercises:
Alter these functions so that they:
1. print 0 when x=0
2. deal with any base
3. return a string instead of print a single digit
"""
