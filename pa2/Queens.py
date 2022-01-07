# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa2
#  Queens.py
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------


def message():
    print("Usage: python3 Queens.py [-v] number", file=sys.stderr)
    print("Option: -v verbose output, print all solutions", file=sys.stderr)
    return
# ------------------------------------------------------------------------------
# definitions of required functions
# ------------------------------------------------------------------------------


def placeQueen(B, i, j):
    B[i][j] = 1
    B[i][0] = j
    for a in range(i+1, len(B)):
        B[a][j] -= 1
    r1, c1 = i+1, j+1
    while r1 <= len(B)-1 and c1 <= len(B)-1:
        B[r1][c1] -= 1
        r1 += 1
        c1 += 1
    r2, c2 = i+1, j-1
    while r2 <= len(B)-1 and c2 > 0:
        B[r2][c2] -= 1
        r2 += 1
        c2 -= 1
    return


def removeQueen(B, i, j):
    B[i][j] = 0
    B[i][0] = 0
    for a in range(i+1, len(B)):
        B[a][j] += 1
    r1, c1 = i+1, j+1
    while r1 <= len(B)-1 and c1 <= len(B)-1:
        B[r1][c1] += 1
        r1 += 1
        c1 += 1
    r2, c2 = i+1, j-1
    while r2 <= len(B)-1 and c2 > 0:
        B[r2][c2] += 1
        r2 += 1
        c2 -= 1
    return


def printBoard(B):
    list = [B[a][0] for a in range(1, len(B))]
    print(tuple(list))
    return


def findSolutions(B, i, mode):
    if i > len(B)-1:
        if mode == "verbose":
            printBoard(B)
        B[0][0] += 1
        return 1
    else:
        for a in range(1, len(B[0])):
            if B[i][a] >= 0:
                placeQueen(B, i, a)
                findSolutions(B, i+1, mode)
                removeQueen(B, i, a)
    return B[0][0]


# ------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------
def main():
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError:
            message()
            exit()
        mode = "not_verbose"
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-v":
            message()
            exit()
        try:
            n = int(sys.argv[2])
        except ValueError:
            message()
            exit()
        mode = "verbose"
    else:
        message()
        exit()
    if n < 1:  # FIX HERE!
        message()
        exit()
    B = [[0 for i in range(0, n+1)] for i in range(0, n+1)]
    sol = findSolutions(B, 1, mode)
    print("{0}-Queens has {1} solutions".format(n, sol))


# end

# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# end
