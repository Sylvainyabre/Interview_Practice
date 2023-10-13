from collections import deque
from abc import ABC, abstractmethod
import copy


class Frontier(ABC):
    @abstractmethod
    def get_next(self)->"Assignment":
        pass

    @abstractmethod
    def add(self, assignment: "Assignment"):
        pass

    @abstractmethod
    def get_length(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class Stack(Frontier):
    def __init__(self):
        self.queue = deque()

    def get_next(self) -> "Assignment":
        return self.queue.pop()

    def add(self, assignment: "Assignment"):
        self.queue.append(assignment)

    def get_length(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return self.get_length() == 0


class Assignment:
    def __init__(self):
        self.nodes = {"A": None, "B": None, "C": None, "D": None,
                      "E": None, "F": None, "G": None, "H": None}
        self.assigned_count = 0

    def get_nodes(self):
        return self.nodes

    def get_prefix(self) -> str:
        empty_prefix = ""
        prefix = "  "
        if self.assigned_count == 1:
            return empty_prefix
        else:
            return prefix*self.assigned_count

    def get_node_value(self, label: str):
        return self.nodes.get(label)

    def add_node(self, label: str, value: int):
        self.nodes[label] = value
        self.assigned_count += 1

    def get_next_unassigned_variable(self):
        for var in list(self.nodes.keys()):
            if self.nodes[var] is None:
                return var
        return None

    def get_assignment_count(self):
        return self.assigned_count

    def is_fully_assigned(self) -> bool:
        for var in list(self.nodes.keys()):
            if self.nodes[var] is None:
                return False
        return True


class assignmentPruningSearchContext:

    def __init__(self, variables, domains):

        self.frontier: Frontier = Stack()
        self.variables: list[str] = variables
        self.domains: list[int] = domains
        self.solution_set = []

    def set_variables(self, variables: list[str]):
        self.variables = variables

    def set_domains(self, doms: list[int]):
        self.domains = doms

    def satisfies_constraints(self, assignment: Assignment) -> bool:
        A = assignment.get_node_value("A")
        B = assignment.get_node_value("B")
        C = assignment.get_node_value("C")
        D = assignment.get_node_value("D")
        E = assignment.get_node_value("E")
        F = assignment.get_node_value("F")
        G = assignment.get_node_value("G")
        H = assignment.get_node_value("H")
        values = list(assignment.get_nodes().values())
        values = list(filter(lambda x: x is not None, values))
        cond_name = ""
        # A>G
        if A is not None and G is not None and A <= G:
            cond_name = "A>G"
            return (False, cond_name)
        # |G-C|=1
        elif G is not None and C is not None and abs(G-C) != 1:
            cond_name = "|G-C|=1"

            return (False, cond_name)
        # D!=C
        elif D is not None and C is not None and D == C:
            cond_name = "D!=C"

            return (False, cond_name)
        # G!=F
        elif G is not None and F is not None and G == F:
            cond_name = "G!=F"
            return (False, cond_name)
        # |E-F| is odd
        elif E is not None and F is not None and abs(E-F) % 2 == 0:
            cond_name = "|E-F| is odd"

            return (False, cond_name)
        # A<=H
        elif A is not None and H is not None and A > H:
            cond_name = "A<=H"

            return (False, cond_name)
        # |H-C| is even
        elif H is not None and C is not None and abs(H-C) % 2 == 1:
            cond_name = "|H-C| is even"

            return (False, cond_name)
        # E != C
        elif E is not None and C is not None and E == C:
            cond_name = "E != C"

            return (False, cond_name)
        # H != F
        elif H is not None and F is not None and H == F:
            cond_name = "H != F"
            return (False, cond_name)
        # |F-B|=1
        elif F is not None and B is not None and abs(F-B) != 1:
            cond_name = "|F-B|=1"

            return (False, cond_name)
        # H !=D
        elif H is not None and D is not None and H == D:
            cond_name = "H !=D"

            return (False, cond_name)
        # E< D-1
        elif E is not None and D is not None and E-D+1 >= 0:
            cond_name = "E< D-1"

            return (False, cond_name)
        # C!=F
        elif C is not None and F is not None and C == F:
            cond_name = "C!=F"
            return (False, cond_name)
        # G < H
        elif G is not None and H is not None and G-H >= 0:
            cond_name = "G < H"

            return (False, cond_name)
        # D>=G
        elif D is not None and G is not None and D < G:
            cond_name = "D>=G"
            return (False, cond_name)
        # E!=H-2
        elif E is not None and H is not None and E == H-2:
            cond_name = "E!=H-2"
            return (False, cond_name)
        # D!=F-1
        elif D is not None and F is not None and F-1 == D:
            cond_name = "D!=F-1"
            return (False, cond_name)

        # At this point all conditions have been satisfied, so we return True
        else:
            return (True, cond_name)

    def search(self, source: str) -> str:
        for d in self.domains:
            initial_assignment = Assignment()
            initial_assignment.add_node(source, d)
            self.frontier.add(initial_assignment)
        failures = 0
        while not self.frontier.is_empty():
            assignment = self.frontier.get_next()
            satisfies_all, _ = self.satisfies_constraints(
                assignment)
            nodes = assignment.get_nodes()
            keys = list(nodes.keys())
            assigned_count = assignment.get_assignment_count()
            next_to_print = keys[assigned_count-1]
            if not satisfies_all:
                failures += 1
                print(
                    f"{assignment.get_prefix()}{next_to_print}={nodes[next_to_print]} failed ")
                continue
            elif assignment.is_fully_assigned():
                print(
                    f"{assignment.get_prefix()}{next_to_print}={nodes[next_to_print]} solution")
                self.solution_set.append(assignment.get_nodes())
            else:
                print(f"{assignment.get_prefix()}{next_to_print}={nodes[next_to_print]} passed")

            next_unassigned_variable = assignment.get_next_unassigned_variable()
            for d in self.domains:
                copy_assignment = copy.deepcopy(assignment)
                if next_unassigned_variable is not None:
                    copy_assignment.add_node(next_unassigned_variable, d)
                    self.frontier.add(copy_assignment)

        print(f"{failures} assignments have failed after")
        return self.solution_set


variables = ["A", "B", "C", "D", "E", "F", "G", "H"]
domains = [1, 2, 3, 4]

searchObj = assignmentPruningSearchContext(variables, domains)
res = searchObj.search("A")
print("SOLUTION_SET: ", res)
