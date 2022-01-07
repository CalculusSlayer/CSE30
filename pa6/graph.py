# ------------------------------------------------------------------------------
#  Nayeel Imtiaz
#  naimtiaz
#  CSE 30-02 Spring 2021
#  pa6
#
#  graph.py
#  - python module containing the graph class and Color function
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# definitions of required functions, classes etc..
# ------------------------------------------------------------------------------
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
        self._color = {}
        for vertex in self._vertices:
            self._color[vertex] = None
        self._ecs = {}
        for vertex in self._vertices:
            self._ecs[vertex] = set()
        self.colors_used = set()

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
            s += '{}: {}\n'.format(x, a[1:-1])
        # end
        return s
    # end

    def add_vertex(self, x):
        """Adds a vertex x to self."""
        if x not in self.vertices:
            self.vertices.append(x)
            self.vertices.sort()
            self._adj[x] = list()
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

    def _find_best(self, L):
        '''
        max = 0
        element = None
        for vertex in L:
           if len(self._ecs[vertex]) >= max:
              element = vertex
        return element
        '''
        '''
      min = 9999999
      element = None
      for vertex in L:
         if len(self._ecs[vertex]) <= min:
             element = vertex
      return element
      '''

        min = 9999999999999
        element = None
        for vertex in L:
            if self.degree(vertex) <= min:
                element = vertex
        return element

        '''
      max = -1
      element = None
      for vertex in L:
         if self.degree(vertex) >= max:
             element = vertex
      return element
      '''

    def _find_best2(self, L):

        _min = 999999
        element_index = None
        for index, vertex in enumerate(L):
            if len(self._ecs[vertex]) <= _min:
                element_index, _min = index, vertex
        return element_index
        '''
      _max = -1
      element_index = None
      for index, vertex in enumerate(L):
         if len(self._ecs[vertex]) >= _max:
            element_index, _max = index, vertex
      return element_index
      '''
    # end

    def Color(self):
        self._color = {}
        self._ecs = {}
        self.colors_used = set()
        for vertex in self._color:
            self._color[vertex] = None
        for vertex in self._vertices:
            self._ecs[vertex] = set()

        if len(self.vertices) == 0:
            return set()
        '''
      for color, vertix in enumerate(self.vertices, start=1):
        self._color[vertix] = color
      list_color = [i for i in range(1, len(self.vertices) + 1)]

      returnable = '{'
      for vertix in list_color:
        returnable += str(vertix)
        if int(self.vertices[-1]) != int(vertix):
           returnable += ", "
      returnable += '}'

      return returnable

      '''
        undiscovered = set(self.vertices)  # undiscovered vertices
        discovered = []             # discovered vertices
        # finished     = set()               # finished vertices
        color_list = [i for i in range(1, len(self.vertices)+1)]
        color_set = set(color_list)

        while len(undiscovered) > 0:
            # discover the source
            source = self._find_best(undiscovered)
            undiscovered.remove(source)        # move source from undiscovered
            discovered.append(source)         # to discovered

            # for vertix in self.vertices:
            #     self._color[vertix] = color_list[0]
            #     self._ecs[vertix] = set()
            # self.colors_used.add(color_list[0])
            while len(discovered) > 0:
                bx = self._find_best2(discovered)
                x = discovered.pop(bx)
                # if x not in self._ecs:
                #     self._ecs[x] = set()
                color = min(color_set.difference(self._ecs[x]))
                self._color[x] = color
                self.colors_used.add(color)
                for y in self._adj[x]:
                    # if y not in self._ecs:
                    #     self._ecs[y] = set()
                    self._ecs[y].add(self._color[x])
                    if y in undiscovered:
                        # self._ecs[y].add(self._color[x])
                        # move y from undiscovered
                        undiscovered.remove(y)
                        discovered.append(y)         # to discovered
                # end
                # end
                # finished.add(x)         # to finished
        colors_used_list = sorted(self.colors_used)
        return set(colors_used_list)
        '''
      returnable = '{'
      for color in colors_used_list:
         returnable += str(color)
         if int(colors_used_list[-1]) != int(color):
            returnable += ', '
      returnable += '}'
      return returnable
      '''
# end

    def getColor(self, x):
        return self._color[x]
