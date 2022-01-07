# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa4
#
#  rational.py
#  - contains code for the rational class
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------
def _gcd(a, b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b


def _lcm(a, b):
    return (a * b) // _gcd(a, b)
# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------


class Rational():
    def __init__(self, n, d=1):
        if d < 0:
            d *= -1
            n *= -1
        self.n = int(n//_gcd(n, d))
        self.d = int(d//_gcd(n, d))

    @property
    def numer(self):
        return self.n

    @property
    def denom(self):
        return self.d

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __repr__(self):
        return "rational.Rational({}, {})".format(self.n, self.d)

    def __float__(self):
        return self.n/self.d

    def __eq__(self, other):
        if self.n/self.d == other.n/other.d:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.n/self.d != other.n/other.d:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.n/self.d < other.n/other.d:
            return True
        else:
            return False

    def __le__(self, other):
        if self.n/self.d <= other.n/other.d:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.n/self.d > other.n/other.d:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.n/self.d >= other.n/other.d:
            return True
        else:
            return False

    def __add__(self, other):
        down = _lcm(self.denom, other.denom)
        mul1 = down//self.denom
        mul2 = down//other.denom
        top = mul1*self.numer + mul2*other.numer
        return Rational(top, down)

    def __sub__(self, other):
        down = _lcm(self.denom, other.denom)
        mul1 = down//self.denom
        mul2 = down//other.denom
        top = mul1*self.numer - mul2*other.numer
        return Rational(top, down)

    def __mul__(self, other):
        top = self.numer * other.numer
        bottom = self.denom * other.denom
        return Rational(top, bottom)

    def __truediv__(self, other):
        top = self.numer * other.denom
        bottom = self.denom * other.numer
        return Rational(top, bottom)

    def inverse(self):
        top = self.denom
        bottom = self.numer
        return Rational(top, bottom)


# ------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
# ------------------------------------------------------------------------------
