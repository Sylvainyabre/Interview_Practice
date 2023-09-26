from collections import deque
from queue import PriorityQueue
from abc import ABC, abstractmethod
import copy


class Node:
    def __init__(self, cost, label):
        self.heuristic_cost = cost
        self.label = label
        self.neighbors = []

    def get_heuristic_cost(self):
        return self.heuristic_cost

    def get_neighbors(self):
        return self.neighbors

    def get_label(self):
        return self.label

    def add_neighbor(self, node):
        self.neighbors.append(node)


class Arc:
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.arc_cost = cost

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_cost(self):
        return self.arc_cost

    def get_total_cost(self):
        return self.get_cost()+self.destination.get_heuristic_cost()


class Frontier(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

class Stack(Frontier):
    def __init__(self):
        self.stack = deque()

    def get_next(self):
        return self.stack.pop()

    def add(self, path):
        self.stack.append(path)

    def get_length(self):
        return len(self.stack)

    def is_empty(self):
        return self.get_length() == 0


class Queue(Frontier):
    def __init__(self):
        self.queue = deque()

    def get_next(self):
        return self.queue.popleft()

    def add(self, path):
        self.queue.append(path)

    def get_length(self):
        return len(self.queue)

    def is_empty(self):
        return self.get_length() == 0


class PriorityQ(Frontier):
    def __init__(self):
        self.pq = PriorityQueue()

    def get_next(self):
        return self.pq.get()

    def add(self, path):
        self.pq.put(path.get_total_cost(), path)

    def get_length(self):
        return self.pq.qsize()

    def is_empty(self):
        return self.get_length() == 0


class HeuristicPriorityQ(Frontier):
    def __init__(self):
        self.pq = PriorityQueue()

    def get_next(self):
        return self.pq.get()

    def add(self, path):
        """Adds paths to the priority queue ordered by heuristic cost

        Args:
            path (Path): The path to be added to the priority q
        """
        self.pq.put(path.get_last_node().get_heuristic_cost(), path)

    def get_length(self):
        return self.pq.qsize()

    def is_empty(self):
        return self.get_length() == 0


class Path:
    def __init__(self):
        self.nodes = []
        self.heuristic_cost = 0
        self.cost = 0

    def get_nodes(self):
        return self.nodes

    def set_cost(self, cost):
        # This is the linear cost of the path, does not include heuristic cost
        self.cost = cost

    def get_cost(self):
        # This is the linear cost of the path, does not include heuristic cost
        return self.cost

    def get_last_node(self):
        # path = [n0,n1,...,nk]
        # return nk
        return self.nodes[len(self.nodes)-1]

    def get_first_node(self):
        # path = [n0,n1,...,nk]
        # return n0
        return self.nodes[0]

    def get_heuristic_cost(self):
        return self.heuristic_cost

    def set_heuristic_cost(self, cost):
        self.heuristic_cost = cost

    def get_total_cost(self):
        return self.cost+self.heuristic_cost

    def add_node(self, node):
        self.nodes.append(node)
        self.set_heuristic_cost(node.get_heuristic_cost())

    def path_string(self):
        labels = list(map(lambda node: node.get_label(), self.nodes))
        return "->".join(labels)


class GenericSearch:
    def __init__(self, goal_func, frontier=Queue()):
        # graph should be a dictionary where keys are nodes
        # and values are lists of neighbors
        self.frontier = frontier
        self.nodes = None
        self.edges = None  # arcs
        self.goal_func = goal_func  # function `goal_func(path,cost,goal)`
        self.cost_map = {}

    def set_frontier(self, new_frontier):
        self.frontier = new_frontier

    def set_goal_func(self, func):
        self.goal_func = func

    def set_graph(self, nodes, edges):
        self.set_nodes(nodes)
        self.set_edges(edges)

    def set_nodes(self, nodes):
        self.nodes = nodes

    def set_edges(self, edges):
        self.edges = edges
        if edges is not None:
            self.set_costs()

    def get_path_linear_cost(self, path):
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
            linear_cost += self.cost_map[cost_key]
        return linear_cost

    def get_cost(self, path):
        source = path.get_first_node()
        destination = path.get_last_node()
        cost_key = "".join([source.get_label(), destination.get_label()])
        cost = self.cost_map[cost_key]
        return cost

    def set_costs(self):
        for edge in self.edges:
            edge_cost = edge.get_total_cost()
            source_label = edge.get_source().get_labe()
            destination_label = edge.get_destination().get_labe()
            key = "".join([source_label, destination_label])
            self.cost_map[key] = edge_cost

    def search(self, source, goal):
        """This generic search function is capable of running BFS, DFS, A*, LCFS,BestFS
        solely based on the data structure it operates on.add()
        - BFS: works with a queue does not consider cost
        - DFS: works with a stack, does not consider cost
        - IDS: works with a stack, does not consider cost
        - A* : works with a priority queue order on f(p) = cost(p)+h(p)
        - BestFS: works with a priority queue, ordered on h(p)
        Args:
            source (Node): The source of the search
            goal (Node): The final node we are trying to find 

        Returns:
            String: A string showing the sequence of nodes leading to the goal node

        """

        self.frontier.add(source)
        steps = 0

        while not self.frontier.is_empty():
            path = self.frontier.get_next()

            last_node = path.get_last_node()
            print(f"Step {steps} : expanding node {last_node.get_label()}")
            steps += 1

            if last_node.get_label() == goal:
                return f"Found path:{path.path_string()} with cost{path.cost()}"
            else:
                last_node = path.get_last_node()
                for neighbor in last_node.get_neighbors():

                    copy_path = copy.copy(path)
                    copy_path.add_node(neighbor)
                    self.frontier.add(copy_path)

        return "No result found"

    def IDS(self):
        self.set_frontier(Queue())
        depth_limit = 0
        while depth_limit:
            pass
