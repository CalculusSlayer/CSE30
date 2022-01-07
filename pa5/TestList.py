
# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa5
#
#  TestList.py
#  - Tests the code in list.py thoroughly with numerous test cases.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
from list import *
# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------


def main():
    # do whatever it is the program is supposed to do
    print()
    print("Testing remove method")
    A = List([11, 1111, 'a', 1, 1, 2, 3, 49, 1, 4, 5, 69, 420, 111, 1111])
    print(A)
    A.remove(1)
    print(A)
    try:
        A.remove(0)
    except ValueError:
        print("Number is not contained in the List object")

    print()
    print("Testing reverse method")
    print(A)
    A.reverse()
    print(A)
    B = List([1, 2])
    print(B)
    B.reverse()
    print(B)

    print()
    print("Testing __getitem__ method")
    C = List([1, 2, 3, 4, 5])
    print(C[0])  # 1
    print(C[4])  # 5
    print(C.__getitem__(-5))  # 1

    print()
    print("Testing __setitem__ method")
    C[2] = 'b'
    print(C)
    print(C[2])

    print()
    print("Testing + method")
    D = List([9, 10])
    E = List([11, 12])
    print(D+E)
    print(D)

    print()
    print("Testing += method")
    F = List(['a', 'b'])
    G = List(['c', 'd'])
    F += G
    print(F)
    D += F
    print(D)
    print(F)

    print()
    print("Testing * method")
    H = List(["cat", "in", "the", "hat"])
    print(H*0)
    print(H*1)
    print(H*3)
    print(H)

    print()
    print("Testing reverse * method")
    I = List(["hi", "there"])
    mult = 3
    print(mult * I)
    print(I * mult)
# end


# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
