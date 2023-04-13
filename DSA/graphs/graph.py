import collections


def BFS(graph, start):
    # There is no recursive way to implement BFS
    queue = collections.deque([])
    visited = set()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
    return visited


def iterativeDFS(graph, start):
    visited = set()
    stack = []
    stack.append(start)
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        for node in graph[current]:
            if node not in visited:
                stack.append(node)
    return visited


def recursiveDFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            recursiveDFS(graph, node)
    return visited


def hasPath(graph, src, dst):
    # use dfs
    visited = set()
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        if current == dst:
            return True
        visited.add(current)
        for node in graph[current]:
            if node not in visited:
                stack.append(node)
    return False


def recursiveHasPath(graph, src, dst, visited=set()):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    for node in graph[src]:
        if recursiveHasPath(graph, node, dst, visited) == True:
            return True
    return False


def makeGraph(edges):
    """Takes an edge list and generate an adjacency list 

    Args:
        edges (2d list): contains edges
    """
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = [a]
        if b not in graph:
            graph[b] = [b]
        # if these nodes exist then add new vertices to them
        graph[a].append(b)
        graph[b].append(a)
    return graph


graph = {"a": ["v", "d", "c"],
         "b": ["e", "f", "v"],
         "c": ["a", "g"],
         "v": ["a", "b", "n"],
         "d": ["a"],
         "n": ["v"],
         "f": ["b"],
         "g": ["c"],
         "e": ["b"]
         }

# print(BFS(graph, "b"))
# print(iterativeDFS(graph, "b"))
# print(recursiveDFS(graph, "b"))
print(recursiveHasPath(graph, "a", "f"))
