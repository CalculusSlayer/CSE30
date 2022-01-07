# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa6
#
#  GraphColoring.py
#  - main file that runs the Color graph function.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# import statements
# ------------------------------------------------------------------------------
from graph import *
import sys


# ------------------------------------------------------------------------------
# definitions of optional helper functions
# ------------------------------------------------------------------------------
def usage():
    print("Usage: $ python3 ContinuedFractions.py <input file> <output file>",
          end='', file=sys.stderr)

# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------


def CheckProperColoring(G):
    for x, y in G._edges:
        if G._color[x] == G._color[y]:
            return False
    return True

# end
# ------------------------------------------------------------------------------
# definition of function main()
# ------------------------------------------------------------------------------


def main():
    try:
        if len(sys.argv) != 3:
            usage()
            exit()
        first = sys.argv[1]
        second = sys.argv[2]
        with open(first, 'r') as f1:
            vertices = f1.readline()
            vertices_list = [i for i in range(1, int(vertices) + 1)]
            edge_list = []
            for line in f1:
                split_line = line.split()
                split_line = tuple(map(int, split_line))
                edge_list.append(split_line)
        G = Graph(vertices_list, edge_list)
        with open(second, 'w') as f2:
            a = G.Color()
            print("{} colors used: {}".format(len(G.colors_used), a), file=f2)
            print(file=f2)
            print("vertex    color", file=f2)
            print("---------------", file=f2)
            for vertex in G.vertices:
                try:
                    print("{:<3}        {:<3}".format(
                        vertex, G._color[vertex]), file=f2)
                except KeyError:
                    print("{:<3}        {:<3}".format(vertex, "None"), file=f2)
            '''
         msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
         print(msg, file=f2)
         '''
    except FileNotFoundError:
        print("[Errno 2] No such file or directory: '{}'".format(
            sys.argv[1]), file=sys.stderr)
        usage()

    '''
   print(G)
   for vertix in G.vertices:
      print(G.getColor(vertix))
# end
   '''


# ------------------------------------------------------------------------------
# closing conditional that calls main()
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
