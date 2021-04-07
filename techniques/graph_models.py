#!/usr/bin/env python
# Finding the shortest path between two points
# Examples from MIT OWC

class Node:
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


# Create nodes and edges example
Boston = Node('Boston')
Providence = Node('Providence')
New_York = Node('New York')
edge1 = Edge(Boston, Providence)
edge2 = Edge(Providence, New_York)
for city in edge1, edge2: print(city)
# Boston->Providence
# Providence->New York


class Digraph:
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' \
                         + dest.getName() + '\n'
        return result[:-1]  # omit final newline


# class Graph(Digraph):
#     def addEdge(self, edge):
#         Digraph.addEdge(self, edge)
#         rev = Edge(edge.getDestination(), edge.getSource())
#         Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# Build graph of cities example
country = buildCityGraph(Digraph)
print(country)
# Boston->Providence
# Boston->New York
# Providence->Boston
# Providence->New York
# New York->Chicago
# Chicago->Denver
# Chicago->Phoenix
# Denver->Phoenix
# Denver->New York
# Los Angeles->Boston


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# Create path example
path1 = [Boston, Providence, New_York]
printPath(path1)
# 'Boston->Providence->New York'


# Depth First Search
# Move down the left branches until either finding
# the destination or a dead end.  If dead end, backtrack
# to the last node with multiple paths and try the next option.
# Recursion is key to continually moving down the left branches.
# 'start' is node that changes from iteration to iteration.
# 'shortest' keeps track of the shortest path, but the search doesn't end
# until all paths are explored.
def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start] # keeps the running path
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end: # if true, the destination has been reached
        return path
    for node in graph.childrenOf(start): # try all the children of the current node
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


# Depth First Search wrapper function
def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


testSP('Chicago', 'Boston')
# Current DFS path: Chicago
# Current DFS path: Chicago->Denver
# Current DFS path: Chicago->Denver->Phoenix
# Current DFS path: Chicago->Denver->New York
# Already visited Chicago
# Current DFS path: Chicago->Phoenix
# There is no path from Chicago to Boston


testSP('Boston', 'Phoenix')
# Current DFS path: Boston
# Current DFS path: Boston->Providence
# Already visited Boston
# Current DFS path: Boston->Providence->New York
# Current DFS path: Boston->Providence->New York->Chicago
# Current DFS path: Boston->Providence->New York->Chicago->Denver
# Current DFS path: Boston->Providence->New York->Chicago->Denver->Phoenix
# Already visited New York
# Current DFS path: Boston->Providence->New York->Chicago->Phoenix
# Current DFS path: Boston->New York
# Current DFS path: Boston->New York->Chicago
# Current DFS path: Boston->New York->Chicago->Denver
# Current DFS path: Boston->New York->Chicago->Denver->Phoenix
# Already visited New York
# Current DFS path: Boston->New York->Chicago->Phoenix
# Shortest path from Boston to Phoenix is Boston->New York->Chicago->Phoenix


printQueue = True

# Breadth First Search
# Consider all the edges that leave a node.
# Follow first edge and check if it ends at the destination.
# If not, check the next edge and repeat.
# Continually removing the oldest element (path) in the pathQueue
# and re-adding this path with an extension to the next node if available.
# Append an extended path for each of the children nodes.
# Because this is BFS, the first successful path found is the shortest.
def BFS(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
        tmpPath = pathQueue.pop(0) # remove the oldest path in the pathQueue
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
        lastNode = tmpPath[-1] # the last node (city) from the previously removed path in the pathQueue
        if lastNode == end:
            return tmpPath # first successful path is the shortest
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath: # tmpPath was the 1st path in the pathQueue before being removed
                newPath = tmpPath + [nextNode] # The old 1st path and nextNode are combined and...
                pathQueue.append(newPath) # re-added to the pathQueue
    return None


# Breadth First Search wrapper function
def shortestPath(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)


testSP('Boston', 'Phoenix')
# Queue: 1
# Boston
# Current BFS path: Boston

# Queue: 2
# Boston->Providence
# Boston->New York
# Current BFS path: Boston->Providence

# Queue: 2
# Boston->New York
# Boston->Providence->New York
# Current BFS path: Boston->New York

# Queue: 2
# Boston->Providence->New York
# Boston->New York->Chicago
# Current BFS path: Boston->Providence->New York

# Queue: 2
# Boston->New York->Chicago
# Boston->Providence->New York->Chicago
# Current BFS path: Boston->New York->Chicago

# Queue: 3
# Boston->Providence->New York->Chicago
# Boston->New York->Chicago->Denver
# Boston->New York->Chicago->Phoenix  <-- The shortest path found here, but 3rd in queue
# Current BFS path: Boston->Providence->New York->Chicago

# Queue: 4
# Boston->New York->Chicago->Denver
# Boston->New York->Chicago->Phoenix  <-- Now 2nd in queue
# Boston->Providence->New York->Chicago->Denver
# Boston->Providence->New York->Chicago->Phoenix
# Current BFS path: Boston->New York->Chicago->Denver

# Queue: 4
# Boston->New York->Chicago->Phoenix  <-- Now 1st in queue
# Boston->Providence->New York->Chicago->Denver
# Boston->Providence->New York->Chicago->Phoenix
# Boston->New York->Chicago->Denver->Phoenix
# Current BFS path: Boston->New York->Chicago->Phoenix

# Shortest path from Boston to Phoenix is Boston->New York->Chicago->Phoenix
