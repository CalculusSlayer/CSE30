# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  la2
#
#  Subset.py
#  - Prints all the k-sized subsets of set of size n.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------
'''
def include_B(B,i):
    B_copy = B.copy()
    B_copy[i] = 1
    return B_copy
    

def exclude_B(B,i):
    B_copy = B.copy()
    B_copy[i] = 0
    return B_copy
'''


def include_L(L, i):
    L.append(i)
    return L


def exclude_L(L):
    L.pop()
    return L


def usage():
    print("Usage: python3 Subset.py n k (where 0<=k<=n)", file=sys.stderr)


# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------
'''
def to_string(B):
    some_list = []
    for index, num in enumerate(B):
        if num == 1:
            some_list.append(index)
    if len(some_list) <= 0:
        return '{ }'
    some_string = '{'
    for val in some_list:
        some_string += str(val)
        if val != some_list[-1]:
            some_string += ', '
    some_string += '}'
    return some_string
'''


def to_string(L):
    """
    Returns the string representation of the subset of {1, 2, ..., n}
    encoded by the list L.
    """
    if len(L) <= 0:
        return '{ }'
    some_string = '{'
    for val in L:
        some_string += str(val)
        if val != L[-1]:
            some_string += ', '
    some_string += '}'
    return some_string


def printSubsets(L, n, k, i):
    """
    Prints all subsets of {1, 2, 3, ..., n} of the form (S union T), where S
    is the subset of {1, 2, 3, ..., (i-1)} encoded by the list L, and T is a
    k-element subset of {i, (i+1), ..., n}.
    """
    if k == 0:
        print(to_string(L))
        return 1
    elif k > (n - i + 1):
        return 0
    else:
        return printSubsets(include_L(L, i), n, k-1, i+1) + printSubsets(exclude_L(L), n, k, i+1)

# ------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------


def main():
   # do whatever it is the program is supposed to do
    if len(sys.argv) != 3:
        usage()
        exit()
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("cannot parse '{}' as int".format(sys.argv[1]), file=sys.stderr)
        usage()
        exit()
    try:
        k = int(sys.argv[2])
    except ValueError:
        print("cannot parse '{}' as int".format(sys.argv[2]), file=sys.stderr)
        usage()
        exit()
    if (0 > k) or (k > n):
        usage()
        exit()
    '''
    B = [0 for i in range(0,n+1)]
    B[0] = '*' 
    printSubsets(B, k, 1)
    '''
    L = []
    printSubsets(L, n, k, 1)

# end


# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
