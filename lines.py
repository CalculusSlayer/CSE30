# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa3
#
#  lines.py
#  Definition of the Point and Line classes.
# ------------------------------------------------------------------------------
import math


# ------------------------------------------------------------------------------
#  Do not change the definition of the Point class, other than to define
#  the function join() at the end.
# ------------------------------------------------------------------------------
class Point(object):
    """Class representing a Point in the x-y coordinate plane."""

    def __init__(self, x, y):
        """Initialize a Point object."""
        self.xcoord = x
        self.ycoord = y
    # end

    def __str__(self):
        """Return the string representation of a Point."""
        return '({}, {})'.format(self.xcoord, self.ycoord)
    # end

    def __repr__(self):
        """Return the detailed string representation of a Point."""
        return 'geometry.Point({}, {})'.format(self.xcoord, self.ycoord)
    # end

    def __eq__(self, other):
        """
        Return True if self and other have the same coordinates, False otherwise.
        """
        eqx = (self.xcoord == other.xcoord)
        eqy = (self.ycoord == other.ycoord)
        return eqx and eqy
    # end

    def distance(self, other):
        """Return the distance between self and other."""
        diffx = self.xcoord - other.xcoord
        diffy = self.ycoord - other.ycoord
        return math.sqrt(diffx**2 + diffy**2)
    # end

    def norm(self):
        """Return the distance from self to the origin (0, 0)."""
        return self.distance(Point(0, 0))
    # end

    def midpoint(self, other):
        """Return the midpoint of the line segment from self to other."""
        midx = (self.xcoord + other.xcoord)/2
        midy = (self.ycoord + other.ycoord)/2
        return Point(midx, midy)
    # end

    # ---------------------------------------------------------------------------
    #  Fill in the definition of this function, belonging to the Point class.
    # ---------------------------------------------------------------------------
    def join(self, other):
        """
        If self==other return None. Otherwise return the line passing through 
        self and other.
        """
        if self.xcoord == other.xcoord and self.ycoord == other.ycoord:
            return None
        else:
            if self.xcoord == other.xcoord:
                slope = 'infinity'
            else:
                slope = (other.ycoord - self.ycoord) / \
                    (other.xcoord - self.xcoord)
            return Line(self, slope)
            pass
        pass
    # end

# end


# ------------------------------------------------------------------------------
#  Fill in the definitions of each method in the Line class.
# ------------------------------------------------------------------------------
class Line(object):
    """Class representing a Line in the x-y coordinate plane."""

    def __init__(self, P, m):
        """Initialize a Line object."""
        self.P = P
        self.m = m
        pass
    # end

    def __str__(self):
        """Return a string representation of a Line."""
        P = self.P
        #m = self.m
        return 'Line through ({}, {}) of slope {}'.format(P.xcoord, P.ycoord, self.m)
        pass
    # end

    def __repr__(self):
        """ Return a detailed string representation of a Line."""
        P = self.P
        # lines.Line(point=(1, 3), slope=-1)
        return 'lines.Line(point=({}, {}), slope={})'.format(P.xcoord, P.ycoord, self.m)
        pass
    # end

    def __eq__(self, other):
        """
        Return True if self and other are identical Lines, False otherwise.
        """
        '''
      if self.P.xcoord == other.P.xcoord and self.P.ycoord == other.P.ycoord and self.m == other.m:
         return True
      else:
         return False
      pass
      '''
        # return self.P.xcoord == other.P.xcoord and self.P.ycoord == other.P.ycoord and self.m == other.m
        if self.m == 'infinity' and other.m != 'infinity':
            return False
        elif self.m != 'infinity' and other.m == 'infinity':
            return False
        elif self.m == 'infinity' and other.m == 'infinity':
            if self.P.xcoord == other.P.xcoord:
                return True
            else:
                return False
        else:
            if (self.m == other.m and (self.m * (0 - self.P.xcoord) + self.P.ycoord) ==
                    (other.m * (0 - other.P.xcoord) + other.P.ycoord)):
                return True
            else:
                return False
    # end

    def parallel(self, other):
        """
        Return True if self and other are parallel lines, False otherwise.
        """
        if self.m == other.m:
            return True
        else:
            return False
    # end

    def perpendicular(self, other):
        """
        Return True if self and other are perpendicular lines, False otherwise.
        """
        if self.m == 0:
            if other.m == 'infinity':
                return True
            else:
                return False
        elif self.m == 'infinity':
            if other.m == 0:
                return True
            else:
                return False
        else:
            if self.m == -1/(other.m):
                return True
            else:
                return False
        pass
    # end

    def contains_point(self, P):
        if self.m == 'infinity':
            if P.xcoord == self.P.xcoord:
                return True
            else:
                return False
        else:
            if self.m*(P.xcoord - self.P.xcoord) + self.P.ycoord == P.ycoord:
                return True
            else:
                return False
        """
      Return True if self contains point P, False otherwise.
      """
        pass
    # end

    def intersect(self, other):
        """
        If self and other are parallel, return None.  Otherwise return their
        Point of intersection.
        """
        if self.m == other.m:
            return None
        elif self.m == 'infinity':
            x = self.P.xcoord
            y = other.m * (x - other.P.xcoord) + other.P.ycoord
            return Point(x, y)
        elif other.m == 'infinity':
            x = other.P.xcoord
            y = self.m * (x - self.P.xcoord) + self.P.ycoord
            return Point(x, y)
        else:
            bottom_determinant = other.m - self.m
            upper_x = (self.P.ycoord - other.P.ycoord - self.m * self.P.xcoord
                       + other.m * other.P.xcoord)
            upper_y = (-self.m * (other.P.ycoord - other.m * other.P.xcoord)
                       - (-other.m * (self.P.ycoord - self.m * self.P.xcoord)))
            return Point(upper_x / bottom_determinant, upper_y / bottom_determinant)
        pass
    # end

    def parallel_line(self, P):
        """Returns the Line through P that is parallel to self."""
        return Line(Point(P.xcoord, P.ycoord), self.m)
        pass
    # end

    def perpendicular_line(self, P):
        """Returns the Line through P that is perpendicular to self."""
        if self.m == 0:
            slope = 'infinity'
        elif self.m == 'infinity':
            slope = 0
        else:
            slope = -1/self.m
        return Line(Point(P.xcoord, P.ycoord), slope)
        pass
    # end

# end


# ------------------------------------------------------------------------------
#  Do not change functon main(). Its role is just to test all of the above.
#  Actually you can change it during your own independent testing, but return
#  it to exactly this state before you submit the project.
# ------------------------------------------------------------------------------
def main():

    P = Point(1, 3)
    Q = Point(3, 3)
    R = Point(1, 1)
    S = Point(3, 1)
    T = Point(4, 3)
    U = Point(5, 5)
    V = Point(2, 2)
    W = Point(2, 5)
    X = Point(2, -1)

    A = Line(P, -1)
    B = Line(R, 1)
    C = S.join(T)  # points_to_line(S, T)
    D = Line(W, 'infinity')
    E = Line(Q, 0)
    F = C.parallel_line(P)

    print()
    print('A =', A)
    print(repr(A))
    print()
    print('B =', B)
    print(repr(B))
    print()
    print('C =', C)
    print(repr(C))
    print()
    print('D =', D)
    print(repr(D))
    print()
    print('E =', E)
    print(repr(E))
    print()
    print('F =', F)
    print(repr(F))

    print()
    print(B.intersect(C) == U)
    print(A.intersect(B) == V)
    print(D.intersect(C) == X)
    print(D.intersect(Line(T, 'infinity')) == None)
    print(A.perpendicular(B))
    print(D.perpendicular(E))
    print(A.parallel(B.perpendicular_line(Q)))
    print(A.contains_point(S))
    print(B.contains_point(U))
    print(C.contains_point(X))
    print(F.contains_point(W))

    print()

# end


# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end

# ------------------------------------------------------------------------------
#  If your Line class and join() method in the Point class are correct, then
#  the output of function main() should be as follows.
# ------------------------------------------------------------------------------
"""

A = Line through (1, 3) of slope -1
lines.Line(point=(1, 3), slope=-1)

B = Line through (1, 1) of slope 1
lines.Line(point=(1, 1), slope=1)

C = Line through (3, 1) of slope 2.0
lines.Line(point=(3, 1), slope=2.0)

D = Line through (2, 5) of slope infinity
lines.Line(point=(2, 5), slope=infinity)

E = Line through (3, 3) of slope 0
lines.Line(point=(3, 3), slope=0)

F = Line through (1, 3) of slope 2.0
lines.Line(point=(1, 3), slope=2.0)

True
True
True
True
True
True
True
True
True
True
True

"""
