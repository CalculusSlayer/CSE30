# ------------------------------------------------------------------------------
#  LineReverse.py
#  Reverses the word order of every line in a file
# ------------------------------------------------------------------------------
import sys

# usage()
# Prints error messages to stderr


def usage():
    print("Usage: $ python3 LineReverse.py <input file> <output file>",
          file=sys.stderr)
    exit()
# end


def main():
    # check command line arguments and open files
    if len(sys.argv) != 3:
        usage()
    # end
    try:
        infile = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        usage()
    # end
    outfile = open(sys.argv[2], 'w')

    # read in each line of infile, reverse it, then print to outfile
    lines = infile.readlines()
    for S in lines:
        L = S.split()
        L.reverse()
        R = ' '.join(L)
        print(R, file=outfile)
    # end

    infile.close()
    outfile.close()

# end


# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
