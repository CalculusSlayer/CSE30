# -------------------------------------------------------------------------------
#  Factorial.py
# -------------------------------------------------------------------------------

def factorial(n):
    """Return n! computed recursively"""

    if n == 0:  # what if n<0
        return 1
    else:
        return n*factorial(n-1)
    # end

# end


# -------------------------------------------------------------------------------
if __name__ == '__main__':

    print()
    print("10! =", factorial(10))
    print("50! =", factorial(50))
    print("75! =", factorial(75))
    print()
    print("100! =", factorial(100))
    print()
    print("997! =", factorial(997))
    print()
    #print("998! =", factorial(998))
    print()

# end
