from queue import deque
graph = {
    "nodes":["1","2","3","4","5","6","7","8"],
    "edges":{"1":["2","6"],"2":["3","1"],"3":["2","7","8"],"4":["5","6","7"],"5":["4","6","8"],"6":["1","3","4","5"],"7":["3","4"],"8":["3","5"]}
}


def countPaths(graph):
    counts = {}
    for node in graph["nodes"]:
        counts[node] = 1
        modifiedBFS(node)
    return counts

def modifiedBFS(source,graph):
    inf = 99999999
    distances = {}
    queue = deque()
    visited = []
    queue.append(graph["nodes"][0])
    for node in graph["nodes"]:
        distances[node] = inf
        
