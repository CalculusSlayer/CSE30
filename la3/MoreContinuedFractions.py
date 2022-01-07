# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  la3
#
#  MoreContinuedFractions.py
#  - this file turns a rational object into a list
#    representation of a continued fraction.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
from rational import *
from decimal import *
import sys
# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------


def CF2R(L):
    if len(L) == 1:
        return Rational(L[0])
    elif len(L) > 1:
        return Rational(L[0]) + CF2R(L[1:]).inverse()


def R2CF(x):
    _list = []
    numer = x.numer
    denom = x.denom
    while True:
        if denom != 0:
            var = numer // denom
        else:
            break
        denom, numer = numer - var * denom, denom
        _list.append(var)
    return _list


def GCF2R(L):
    if len(L) == 1:
        return Rational(L[0])
    elif len(L) == 0:
        return Rational(1)
    elif len(L) > 1:
        return Rational(L[0]) + Rational(L[1])/GCF2R(L[2:])


def pi_gen():
    yield 0
    yield 4
    k = 1
    while True:
        yield 2*k-1
        yield k**2
        k += 1
# ------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------


def main():
    # do whatever it is the program is supposed to do
    '''
    print("Testing the CF2R function and R2CF function")
    print(CF2R([7,5,10,3]))
    print(CF2R([7,5,4]))
    print(CF2R([7,5,3,1]))
    print(R2CF(Rational(1137,158)))
    print(R2CF(Rational(151,21)))

    print("Doing inverse tests")
    print(R2CF(CF2R([7,5,10,3])) == [7, 5, 10, 3])
    print(R2CF(CF2R([7,5, 4])) == [7, 5, 4])
    print(CF2R(R2CF(Rational(1137,158)))==Rational(1137,158))
    print(CF2R(R2CF(Rational(151,21)))==Rational(151,21))

    print("new")
    print(GCF2R([1,2,3,4,5]))
    print(GCF2R([0,4,1,1,3,4,5,9,7]))
    print(GCF2R([1,2,3,4]))
    print(GCF2R([1,2,3]))
    print(GCF2R([1,2]))

    print("test pi generator")
    '''
    count = 0
    list_pi = []
    for i in pi_gen():
        if count <= 267:
            list_pi.append(i)
            count += 1
        else:
            break
    pi_object = GCF2R(list_pi)
    print()
    print(pi_object)
    print()
    getcontext().prec = 101
    print(Decimal(pi_object.numer)/Decimal(pi_object.denom))
    print()
    print(list_pi)
    print()


# end

# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
