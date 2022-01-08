# ------------------------------------------------------------------------------
#  graphs.py
#  Definition of the Graph class.
# ------------------------------------------------------------------------------
from queue import *


class Graph(object):
    """Class representing an undirected graph."""

    def __init__(self, V, E):
        """Initialize a Graph object."""

        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._edges = list(E)
        self._adj = {x: list() for x in V}
        for e in E:
            x, y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
        # end

        # additional attributes
        self._component = {x: None for x in V}   # for findComponents()
        self._distance = {x: None for x in V}    # for BFS()
        self._predecessor = {x: None for x in V}  # for BFS()

    # end

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices
    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges
    # end

    def __str__(self):
        """Return a string representation of self."""
        s = ''
        for x in self.vertices:
            a = str(self._adj[x])
            s += f'{x}: {a[1:-1]}\n'
        # end
        return s
    # end

    def add_vertex(self, x):
        """Adds a vertex x to self."""
        if x not in self.vertices:
            self.vertices.append(x)
            self.vertices.sort()
            self._adj[x] = list()
            self._component[x] = None
            self._distance[x] = None
            self._predecessor[x] = None
        # end
    # end

    def add_edge(self, e):
        """Adds an edge e to self."""
        x, y = tuple(e)
        self.add_vertex(x)
        self.add_vertex(y)
        self._adj[x].append(y)
        self._adj[y].append(x)
        self._adj[x].sort()
        self._adj[y].sort()
        self.edges.append(e)
    # end

    def degree(self, x):
        """Returns the degree of vertex x."""
        return len(self._adj[x])
    # end

    def reachable(self, source):
        """Return the set of vertices that are reachable from source."""

        # initialize
        undiscovered = set(self.vertices)  # undiscovered vertices
        discovered = Queue()             # discovered vertices
        finished = set()               # finished vertices

        # discover the source
        undiscovered.remove(source)        # move source from undiscovered
        discovered.enqueue(source)         # to discovered

        # discover all vertices reachable from the source
        while not discovered.isEmpty():
            x = discovered.dequeue()        # move x from discovered
            for y in self._adj[x]:
                if y in undiscovered:
                    undiscovered.remove(y)        # move y from undiscovered
                    discovered.enqueue(y)         # to discovered
                # end
            # end
            finished.add(x)                 # to finished
        # end
        return finished
    # end

    def findComponents(self):
        """Assign an int to each connected component of self."""
        completed = set()
        count = 0
        for s in self.vertices:
            if not s in completed:
                count += 1
                finished = self.reachable(s)
                for x in finished:
                    self._component[x] = count
                # end
                # completed = completed.union(finished)
                completed.update(finished)
            # end
        # end
    # end

    def getComponent(self, x):
        """Return the component label of vertex x."""
        return self._component[x]
    # end

    def getDistance(self, x):
        """Return the distance from (most recent) source to x."""
        return self._distance[x]
    # end

    def getPredecessor(self, x):
        """
        Return the predecessor of x in a shortest path from the (most recent) 
        source to x.
        """
        return self._predecessor[x]
    # end

    def sameComponent(self, x, y):
        """
        Return True if x and y belong to the same connected component of self,
        otherwise return False. Pre: must call findComponents() first.
        """
        for v in self.vertices:
            if not self._component[v]:
                msg = 'Not all vertices have a component label'
                raise ValueError(msg)
            # end
        # end
        return (self._component[x] == self._component[y])
    # end

    def BFS(self, source):
        """
        Run the Breadth First Search algorithm, finding distances from source
        to all other vertices.
        """

        # initialize
        undiscovered = set(self.vertices)  # undiscovered vertices
        discovered = Queue()             # discovered vertices
        finished = set()               # finished vertices
        for v in self.vertices:
            self._distance[v] = 'Infinity'
            self._predecessor[v] = None
        # end

        # discover the source
        undiscovered.remove(source)        # move source from undiscovered
        discovered.enqueue(source)         # to discovered
        self._distance[source] = 0

        # discover everything reachable from the source
        while not discovered.isEmpty():
            x = discovered.dequeue()        # move x from discovered
            for y in self._adj[x]:
                if y in undiscovered:
                    undiscovered.remove(y)        # move y from undiscovered
                    discovered.enqueue(y)         # to discovered
                    self._distance[y] = self._distance[x]+1   # set distance
                    self._predecessor[y] = x                  # set predecessor
                # end
            # end
            finished.add(x)                 # to finished
        # end
        # return finished  # don't need to return anything
    # end

    def getPath(self, source, x, L):
        """
        Appends the vertices of a shortest source-x path to L. Pre: BFS() was 
        most recently run on source.
        """
        if self._distance[source] != 0:
            msg = 'Must run BFS() on '+str(source)+' before calling getPath()'
            raise ValueError(msg)
        # end

        if x == source:
            L.append(source)
        elif not self._predecessor[x]:
            L.append(str(x)+' not reachable from '+str(source))
        else:
            self.getPath(source, self._predecessor[x], L)
            L.append(x)
        # end
    # end


# end


# ------------------------------------------------------------------------------
#  Test the Graph type
# ------------------------------------------------------------------------------
def main():

    V = [1, 2, 3, 4, 5, 6]
    E = [(1, 2), (1, 4), (2, 3), (2, 4), (2, 5),
         (3, 5), (3, 6), (4, 5), (5, 6)]
    G = Graph(V, E)

    print()
    print(G.vertices)
    print(G.edges)
    print()
    print(G)

    G.add_edge((7, 8))
    G.add_edge((7, 9))
    G.add_edge((8, 9))

    print(G.vertices)
    print(G.edges)
    print()
    print(G)

    # test reachable()
    print(G.reachable(1))
    print(G.reachable(7))
    print()

    H = Graph('abcdef', ['ab', 'ad', 'bc', 'bd', 'be', 'bf', 'cf', 'de', 'ef'])
    print(H.vertices)
    print(H.edges)
    print()
    print(H)
    print()
    print(H.reachable('d'))
    print()

    # test findComponents() and getComponent()
    print('component containing {}: {}'.format(2, G.getComponent(2)))
    print('component containing {}: {}'.format(8, G.getComponent(8)))
    # print(G.sameComponent(2, 8)) # raises ValueError
    print()
    G.findComponents()
    print('component containing {}: {}'.format(2, G.getComponent(2)))
    print('component containing {}: {}'.format(8, G.getComponent(8)))
    print('{} reachable from {} is {}'.format(2, 8, G.sameComponent(2, 8)))
    print()

    # test BFS() and getPath
    G.BFS(1)
    L = list()
    G.getPath(1, 6, L)
    for v in G.vertices:
        print(v, G.getDistance(v), G.getPredecessor(v))
    # end
    print(L)
    G.getPath(1, 9, L)
    print(L)
    print()

# end


# ------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

# end
