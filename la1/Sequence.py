# -----------------------------------------------------------------
# Nayeel Imtiaz
# naimtiaz
# CSE 30-02 Spring 2021
# la1
# Sequence.py
# -----------------------------------------------------------------

# ---------------------------------------------------------------
# import statements
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# definition of optional helper functions
# ---------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# definition of required functions

def power_remainder(n, m, r):
    """
    Returns a generator of the (infinite) sequence of positive integers that 
    are (1) exact powers of n and (2) have remainder r upon division by m.
    """
    k = 1
    while True:
        value = k ** n
        if value % m == r:
            yield value
        k += 1
# end


def common_terms(g, h):
    """
    Returns a generator of the sequence of terms that are common to the two 
    (increasing) sequences produced by generators g and h.
    """
    i = next(g)
    j = next(h)
    while True:
        if i < j:
            i = next(g)
        elif j < i:
            j = next(h)
        else:
            yield i
            i = next(g)
            j = next(h)
# end
# end
# ---------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# definition of function main()


def main():

    A = power_remainder(2, 3, 1)
    B = power_remainder(3, 5, 4)
    C = common_terms(power_remainder(2, 3, 1), power_remainder(3, 5, 4))

    print()
    for i in range(15):
        s = "  {0:<12}{1:<12}{2:<12}".format(next(A), next(B), next(C))
        print(s)
    # end
    print()

# end

# -------------------------------------------------------------------------------
# closing condition that calls main


if __name__ == '__main__':

    main()

# end

    """
    Expected output:

    1           64          64
    4           729         117649
    16          2744        262144
    25          6859        4826809
    49          13824       24137569
    64          24389       113379904
    100         39304       148035889
    121         59319       481890304
    169         85184       1073741824
    196         117649      2565726409
    256         157464      3010936384
    289         205379      6321363049
    361         262144      10779215329
    400         328509      19770609664
    484         405224      22164361129

    """
# ----------------------------------------------------------------------------------
