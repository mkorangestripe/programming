# Graphs and Models

This finds the shortest path between two points in a graph of cities.

### Nodes and Edges

```python
class Node:
    """Create nodes(cities)"""

    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge:
    """Create edges(paths)"""

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
```

```python
Boston = Node('Boston')
Providence = Node('Providence')
New_York = Node('New York')

edge1 = Edge(Boston, Providence)
edge2 = Edge(Providence, New_York)

for edge in edge1, edge2:
    print(edge)
```

```
Boston->Providence
Providence->New York
```

### Graphs

```python
class Digraph:
    """
    Template for the graph of cities.
    The 'edges' dictionary maps each node to a list of its children.
    """

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
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


def buildCityGraph(graphType):
    """Instantiate the graph and add nodes(cities) and edges(paths)"""

    graph = graphType()

    # Create a node for each city:
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        graph.addNode(Node(name))

    graph.addEdge(Edge(graph.getNode('Boston'), graph.getNode('Providence')))
    graph.addEdge(Edge(graph.getNode('Boston'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('Providence'), graph.getNode('Boston')))
    graph.addEdge(Edge(graph.getNode('Providence'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('New York'), graph.getNode('Chicago')))
    graph.addEdge(Edge(graph.getNode('Chicago'), graph.getNode('Denver')))
    graph.addEdge(Edge(graph.getNode('Chicago'), graph.getNode('Phoenix')))
    graph.addEdge(Edge(graph.getNode('Denver'), graph.getNode('Phoenix')))
    graph.addEdge(Edge(graph.getNode('Denver'), graph.getNode('New York')))
    graph.addEdge(Edge(graph.getNode('Los Angeles'), graph.getNode('Boston')))

    return graph
```

```python
# Build the graph of cities:
country = buildCityGraph(Digraph)
print(country)
```

```
Boston->Providence
Boston->New York
Providence->Boston
Providence->New York
New York->Chicago
Chicago->Denver
Chicago->Phoenix
Denver->Phoenix
Denver->New York
Los Angeles->Boston
```

```python
def printPath(path):
    """Assumes path is a list of nodes"""

    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'

    return result
```

```python
# Create a path:
path1 = [Boston, Providence, New_York]
printPath(path1)
```

```
'Boston->Providence->New York'
```

### Depth First Search

Move down the left branches until either finding the destination or a dead end.  
If dead end, backtrack to the last node with multiple paths and try the next option.

The 'start' node changes from iteration to iteration.  
The 'shortest' keeps track of the shortest path, but the search doesn't end until all paths are explored.

```python
def DFS(graph, start, end, path, shortest, toPrint=False):
    """
    Depth First Search
    Assume graph is a Digraph, start and end are nodes, path and shortest are lists of nodes.
    Return the shortest path from start to end in the graph.
    """

    path = path + [start]  # keeps the running path

    if toPrint:
        print('Current DFS path:', printPath(path))

    if start == end:  # if true, the destination has been reached
        return path

    for node in graph.children_of(start):  # try all children of the current node
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)

    return shortest

def shortestPath(graph, start, end, toPrint=False):
    """
    Wrapper function for DFS()
    Assume graph is a Digraph; start and end are nodes.
    Return the shortest path from start to end in the graph.
    """
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    """
    Instantiate the graph of cities.
    Call shortestPath() and print the shortest path if found.
    """

    graph = buildCityGraph(Digraph)

    sp = shortestPath(graph,
                      graph.getNode(source),
                      graph.getNode(destination),
                      toPrint = True)

    if sp is not None:
        print('Shortest path from', source, 'to',
               destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)
```

```python
testSP('Chicago', 'Boston')
```

```
Current DFS path: Chicago
Current DFS path: Chicago->Denver
Current DFS path: Chicago->Denver->Phoenix
Current DFS path: Chicago->Denver->New York
Already visited Chicago
Current DFS path: Chicago->Phoenix
There is no path from Chicago to Boston
```

```python
testSP('Boston', 'Phoenix')
```

```
Current DFS path: Boston
Current DFS path: Boston->Providence
Already visited Boston
Current DFS path: Boston->Providence->New York
Current DFS path: Boston->Providence->New York->Chicago
Current DFS path: Boston->Providence->New York->Chicago->Denver
Current DFS path: Boston->Providence->New York->Chicago->Denver->Phoenix
Already visited New York
Current DFS path: Boston->Providence->New York->Chicago->Phoenix
Current DFS path: Boston->New York
Current DFS path: Boston->New York->Chicago
Current DFS path: Boston->New York->Chicago->Denver
Current DFS path: Boston->New York->Chicago->Denver->Phoenix
Already visited New York
Current DFS path: Boston->New York->Chicago->Phoenix
Shortest path from Boston to Phoenix is Boston->New York->Chicago->Phoenix
```

### Breadth First Search

Consider all the edges connected to a node.  
Follow first edge and check if it ends at the destination.  
If not, check the next edge and repeat.  
Continually removing the oldest element (path) in the pathQueue and re-adding this path with an extension to the next node if available.  
Append an extended path for each of the children nodes.  
Because this is BFS, the first successful path found is the shortest.

```python
PRINT_QUEUE = True

def BFS(graph, start, end, toPrint=False):
    """
    Breadth First Search
    Assume graph is a Digraph; start and end are nodes
    Return the shortest path from start to end in the graph.
    """

    initPath = [start]
    pathQueue = [initPath]

    # Get and remove oldest element in pathQueue:
    while len(pathQueue) != 0:
        if PRINT_QUEUE:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
        tmpPath = pathQueue.pop(0)  # remove the oldest path in the pathQueue
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
        lastNode = tmpPath[-1]  # the last node (city) from the previously removed path in the pathQueue
        if lastNode == end:
            return tmpPath  # first successful path is the shortest
        for nextNode in graph.children_of(lastNode):
            if nextNode not in tmpPath:  # tmpPath was the 1st path in the pathQueue before being removed
                newPath = tmpPath + [nextNode]  # the old 1st path and nextNode are combined and...
                pathQueue.append(newPath)  # re-added to the pathQueue

    return None

def shortestPath(graph, start, end, toPrint=False):
    """
    Wrapper function for BFS()
    Assume graph is a Digraph; start and end are nodes.
    Return the shortest path from start to end in the graph.
    """
    return BFS(graph, start, end, toPrint)
```

```python
testSP('Boston', 'Phoenix')
```

```
Queue: 1
Boston
Current BFS path: Boston

Queue: 2
Boston->Providence
Boston->New York
Current BFS path: Boston->Providence

Queue: 2
Boston->New York
Boston->Providence->New York
Current BFS path: Boston->New York

Queue: 2
Boston->Providence->New York
Boston->New York->Chicago
Current BFS path: Boston->Providence->New York

Queue: 2
Boston->New York->Chicago
Boston->Providence->New York->Chicago
Current BFS path: Boston->New York->Chicago

Queue: 3
Boston->Providence->New York->Chicago
Boston->New York->Chicago->Denver
Boston->New York->Chicago->Phoenix
Current BFS path: Boston->Providence->New York->Chicago

Queue: 4
Boston->New York->Chicago->Denver
Boston->New York->Chicago->Phoenix
Boston->Providence->New York->Chicago->Denver
Boston->Providence->New York->Chicago->Phoenix
Current BFS path: Boston->New York->Chicago->Denver

Queue: 4
Boston->New York->Chicago->Phoenix
Boston->Providence->New York->Chicago->Denver
Boston->Providence->New York->Chicago->Phoenix
Boston->New York->Chicago->Denver->Phoenix
Current BFS path: Boston->New York->Chicago->Phoenix

Shortest path from Boston to Phoenix is Boston->New York->Chicago->Phoenix
```
