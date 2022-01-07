
# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa1
#
#  Subset.py
#  a very short description of what the file contains
# ------------------------------------------------------------------------------

import sys


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
            some_string += ','
    some_string += '}'
    return some_string


def printSubsets(B, k, i):
    if k == 0:
        print(to_string(B))
        return 1
    elif k > ((len(B)-1) - i + 1):
        return 0
    else:
        return printSubsets(include_B(B, i), k-1, i+1) + printSubsets(exclude_B(B, i), k, i+1)


def include_B(B, i):
    B_copy = B.copy()
    B_copy[i] = 1
    return B_copy


def exclude_B(B, i):
    B_copy = B.copy()
    B_copy[i] = 0
    return B_copy


def main():
    if len(sys.argv) != 3:
        exit()
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    except ValueError:
        exit()
    if (0 > k) or (k > n):
        exit()
    B = [0 for i in range(0, n+1)]
    B[0] = '*'
    printSubsets(B, k, 1)


if __name__ == '__main__':
    main()
