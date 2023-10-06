from collections import deque
from queue import PriorityQueue
from abc import ABC, abstractmethod
import copy
from typing import Callable


class Node:
    def __init__(self, cost: int, label: str):
        self.heuristic_cost: int = cost
        self.label: str = label
        self.neighbors: list[Node] = []

    def __str__(self) -> str:
        return self.label

    def get_heuristic_cost(self) -> int:
        return self.heuristic_cost

    def get_neighbors(self) -> list["Node"]:
        return self.neighbors

    def get_label(self) -> str:
        return self.label

    def add_neighbor(self, node: "Node"):
        self.neighbors.append(node)


class Arc:
    def __init__(self, source: Node, destination: Node, cost: int):
        self.source: Node = source
        self.destination: Node = destination
        self.arc_cost: int = cost

    def get_source(self) -> Node:
        return self.source

    def get_destination(self) -> Node:
        return self.destination

    def get_cost(self) -> int:
        return self.arc_cost

    def get_total_cost(self) -> int:
        return self.get_cost()+self.destination.get_heuristic_cost()


class Frontier(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def add(self, node: Node):
        pass

    @abstractmethod
    def get_length(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class Stack(Frontier):
    def __init__(self):
        self.stack = deque()

    def get_next(self) -> Node:
        return self.stack.pop()

    def add(self, path: "Path"):
        self.stack.append(path)

    def get_length(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return self.get_length() == 0


class Queue(Frontier):
    def __init__(self):
        self.queue = deque()

    def get_next(self) -> Node:
        return self.queue.popleft()

    def add(self, path: "Path"):
        self.queue.append(path)

    def get_length(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return self.get_length() == 0


class PriorityQ(Frontier):
    """This priority has three modes:
    - `linear_mode`: when this is active, the priority queue only uses the cost of the path as priority value
    - `heuristic_mode`: when this is active, the heuristic value of each path is used as priority value
    - `total_mode`: when this is active, the value f(p = h(p)+cost(p) is used as the priority value

    * To perform LCFS: activate `linear_mode` before passing it to the search object
    * To perform A* : activate `total_mode` before passing it to the search object
    * to perform BestFS: activate `heuristic_mode` before passing it to the search object

    """

    def __init__(self):
        self.pq = PriorityQueue()
        self.priority_mode = "linear_mode"
        self.HEURISTIC_MODE = "heuristic_mode"
        self.LINEAR_MODE = "linear_mode"
        self.TOTAL_MODE = "total_mode"

    def get_next(self) -> Node:
        path = self.pq.get()

        return path

    def add(self, path: "Path"):
        if self.is_linear_mode_active():
            path.activate_linear_cost_comparison()
        elif self.is_heuristic_mode_active():
            path.activate_heuristic_cost_comparison()
        else:
            path.activate_total_cost_comparison()
        self.pq.put(path)

    def get_length(self) -> int:
        return self.pq.qsize()

    def is_empty(self) -> bool:
        return self.get_length() == 0

    def activate_linear_cost_mode(self):
        self.priority_mode = self.LINEAR_MODE

    def activate_total_cost_mode(self):
        self.priority_mode = self.TOTAL_MODE

    def activate_heuristic_cost_mode(self):
        self.priority_mode = self.HEURISTIC_MODE

    def is_linear_mode_active(self) -> bool:
        return self.priority_mode == self.LINEAR_MODE

    def is_total_mode_active(self) -> bool:
        return self.priority_mode == self.TOTAL_MODE

    def is_heuristic_mode_active(self) -> bool:
        return self.priority_mode == self.HEURISTIC_MODE


class Path:
    def __init__(self):
        self.comparison_mode = "linear_mode"
        self.nodes: list[Node] = []
        self.heuristic_cost: int = 0
        self.cost: int = 0
        self.HEURISTIC_MODE = "heuristic_mode"
        self.LINEAR_MODE = "linear_mode"
        self.TOTAL_MODE = "total_mode"

    def get_nodes(self) -> list[Node]:
        return self.nodes

    def set_cost(self, cost: int):
        """This sets the linear cost of the path, does not include heuristic cost"""
        self.cost = cost

    def get_cost(self) -> int:
        """This returns the linear cost of the path, does not include heuristic cost"""
        return self.cost

    def get_last_node(self) -> Node:
        # path = [n0,n1,...,nk]
        # return nk
        return self.nodes[len(self.nodes)-1]

    def get_first_node(self) -> Node:
        # path = [n0,n1,...,nk]
        # return n0
        return self.nodes[0]

    def get_heuristic_cost(self) -> int:
        return self.heuristic_cost

    def set_heuristic_cost(self, cost: int):
        self.heuristic_cost = cost

    def get_total_cost(self) -> int:
        return self.cost+self.heuristic_cost

    def add_node(self, node: Node):
        self.nodes.append(node)
        self.set_heuristic_cost(node.get_heuristic_cost())

    def path_string(self) -> str:
        labels = list(map(lambda node: node.get_label(), self.nodes))
        return "->".join(labels)

    def activate_linear_cost_comparison(self):
        self.comparison_mode = self.LINEAR_MODE

    def activate_heuristic_cost_comparison(self):
        self.comparison_mode = self.HEURISTIC_MODE

    def activate_total_cost_comparison(self):
        self.comparison_mode = self.TOTAL_MODE

    def __lt__(self, other: "Path"):
        if self.comparison_mode == self.LINEAR_MODE:
            return self.get_cost() < other.get_cost()
        elif self.comparison_mode == self.HEURISTIC_MODE:
            return self.get_heuristic_cost() < other.get_heuristic_cost()
        else:
            return self.get_total_cost() < other.get_total_cost()

class GenericSearchContext:
    """This is a multipurpose search context capable of performing DFS, BFS, LCFS, BestFS, A*
    by calling `search(source:Node,goal:str)` after configuring and setting the relevant data structure
    - To perform BFS, set the frontier to an instance of Queue
    - To perform DFS, set the frontier to an instance of Stack
    - To perform LCFS: activate `linear_mode` before passing it to the search object
    - To perform A* : activate `total_mode` before passing it to the search object
    - to perform BestFS: activate `heuristic_mode` before passing it to the search object
    """

    def __init__(self, frontier=Queue()):

        self.frontier: list[Frontier] = frontier
        self.nodes: list[Node] = None
        self.edges: list[Arc] = None  # arcs
        self.cost_map = {}
        self.depth_bound = 0
        self.is_depth_bound_reached = False
        self.solution_so_far = None
        self.cost_so_far = 99999999

    def set_frontier(self, new_frontier: Frontier):
        self.frontier = new_frontier

    def set_graph(self, nodes: list[Node], edges: list[Arc]):
        self.set_nodes(nodes)
        self.set_edges(edges)

    def set_nodes(self, nodes: list[Node]):
        self.nodes = nodes

    def set_edges(self, edges: list[Arc]):
        self.edges = edges
        if edges is not None:
            self.set_costs()

    def get_path_linear_cost(self, path: Path) -> int:
        # list cost of the path not including heuristics
        # ``path.get_nodes() returns [n0,n1,...,nk]``
        linear_cost = 0
        nodes = path.get_nodes()
        idx = 1
        while idx < len(nodes):
            source_node = nodes[idx-1]
            dest_node = nodes[idx]
            source_label = source_node.get_label()
            dest_label = dest_node.get_label()
            cost_key = "".join([source_label, dest_label])
            linear_cost += self.cost_map[cost_key] - \
                dest_node.get_heuristic_cost()
            idx += 1
        return linear_cost

    def get_cost(self, path: Path) -> int:
        path_cost = 0

        source = path.get_first_node()
        destination = path.get_last_node()
        cost_key = "".join([source.get_label(), destination.get_label()])
        path_cost += self.cost_map[cost_key]
        return path_cost

    def set_costs(self):
        for edge in self.edges:
            edge_cost = edge.get_total_cost()
            source_label = edge.get_source().get_label()
            destination_label = edge.get_destination().get_label()
            key = "".join([source_label, destination_label])
            self.cost_map[key] = edge_cost

    def search(self, source: Node, goal: str) -> str:
        """This generic search function is capable of running BFS, DFS, A*, LCFS,BestFS
        solely based on the data structure it operates on .add()
        ------------------------------------------------
        - BFS: works with a queue does not consider cost
        - DFS: works with a stack, does not consider cost
        - IDS: works with a stack, does not consider cost
        - LCFS: works with a priority queue ordered by cost(p)
        - A* : works with a priority queue order on f(p) = cost(p)+h(p)
        - BestFS: works with a priority queue, ordered on h(p)
        -----------------------------------------
        - Args:
            source (Node): The source of the search
            goal (Node): The final node we are trying to find

        Returns:
            String: A string showing the sequence of nodes leading to the goal node

        """
        initial_path = Path()
        initial_path .add_node(source)
        initial_path.set_cost(self.get_path_linear_cost(initial_path))
        self.frontier.add(initial_path)
        steps = 0

        while not self.frontier.is_empty():
            path = self.frontier.get_next()
            last_node = path.get_last_node()
            print("--------------------------------------------")
            print(f"Step {steps} : expanding node {last_node.get_label()}")

            steps += 1
            if last_node.get_label() == goal:

                return f"Found path:{path.path_string()} with cost {self.get_path_linear_cost(path)}"

            last_node = path.get_last_node()
            for neighbor in last_node.get_neighbors():

                copy_path = copy.deepcopy(path)
                copy_path.add_node(neighbor)
                copy_path.set_cost(self.get_path_linear_cost(copy_path))
                self.frontier.add(copy_path)

        return "No result found"

    def IDS(self, source: Node, goal: str):
        self.set_frontier(Queue())
        depth_limit = 0
        self.search()


A = Node(21, "A")
B = Node(19, "B")
C = Node(19, "C")
D = Node(9, "D")
E = Node(11, "E")
F = Node(12, "F")
G = Node(4, "G")
H = Node(6, "H")
S = Node(24, "S")
Z = Node(0, "Z")

A.add_neighbor(C)
B.add_neighbor(C)
C.add_neighbor(D)
C.add_neighbor(E)
C.add_neighbor(F)
D.add_neighbor(F)
E.add_neighbor(F)
F.add_neighbor(G)
F.add_neighbor(H)
F.add_neighbor(Z)
G.add_neighbor(Z)
H.add_neighbor(Z)
S.add_neighbor(A)
S.add_neighbor(B)
S.add_neighbor(C)

nodes = [A, B, C, D, E, F, G, H, S, Z]

SA = Arc(S, A, 3)
SC = Arc(S, C, 4)
SB = Arc(S, B, 9)
AC = Arc(A, C, 2)
BC = Arc(B, C, 13)
CD = Arc(C, D, 5)
CE = Arc(C, E, 4)
CF = Arc(C, F, 8)
DF = Arc(D, F, 5)
EF = Arc(E, F, 7)
FG = Arc(F, G, 8)
FH = Arc(F, H, 7)
FZ = Arc(F, Z, 18)
HZ = Arc(H, Z, 6)
GZ = Arc(G, Z, 9)
edges = [SA, SB, SC, AC, BC, CD, CE, CF, DF, EF, FG, FH, FZ, HZ, GZ]

stack = Stack()
queue = Queue()
pq = PriorityQ()
pq.activate_linear_cost_mode()
searchObj = GenericSearchContext()
searchObj.set_nodes(nodes)
searchObj.set_edges(edges)
searchObj.set_frontier(pq)
res = searchObj.search(S, "Z")
print(res)
