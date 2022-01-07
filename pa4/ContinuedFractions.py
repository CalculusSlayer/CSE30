# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa4
#
#  ContinuedFractions.py
#  - contains code for printing a continued fraction.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
import sys
from decimal import *
from rational import *
# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------


def usage():
    print("Usage: $ python3 ContinuedFractions.py <input file> <output file>",
          end='', file=sys.stderr)
    #sys.stderr.write("Usage: $ python3 ContinuedFractions.py <input file> <output file>")
# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------


def CF(L):
    if len(L) == 1:
        return Rational(L[0])
    elif len(L) > 1:
        return Rational(L[0]) + CF(L[1:]).inverse()

# ------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------


def main():
    if len(sys.argv) != 3:
        usage()
        exit()

    getcontext().prec = 100
    first = sys.argv[1]  # in1.txt
    second = sys.argv[2]  # out1.txt
    try:
        with open(first, 'r') as f1, open(second, 'w') as f2:
            for line in f1:
                split_line = line.split()
                split_list = list(map(int, split_line))
                apple = CF(split_list)
                print('', file=f2)
                print(str(apple), file=f2)
                print(Decimal(apple.numer)/Decimal(apple.denom), file=f2)

    except FileNotFoundError:
        print("[Errno 2] No such file or directory: '{}'".format(
            sys.argv[1]), file=sys.stderr)
        #sys.stderr.write("[Errno 2] No such file or directory: '{}'\n".format(sys.argv[1]))
        usage()


# end

# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
