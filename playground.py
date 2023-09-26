# from queue import PriorityQueue


# pq = PriorityQueue()


# write a function to print all permutations of a string
# def permute(s):
#     out = []
#     if len(s) == 1:
#         out = [s]
#     else:
#         for i, t in enumerate(s):
#             for perm in permute(s[:i] + s[i+1:]):
#                 out += [t + perm]
#     return out


def printMatrix(matrix):
    for row in matrix:
        joined_row = " ".join(row)
        print(joined_row, end="\n")


mtx = [["x", "x", "x", "x",  "x", "x", "x", "o"],
       ["o", "o", "o", "o",  "o", "o", "o", "x"],
       ["o", "o", "o", "o",  "o", "o", "x", "o"],
       ["o", "o", "o", "x",  "x", "o", "o", "o"],
       ["o", "o", "x", "o",  "x", "o", "o", "x"],
       ["x", "o", "o", "o",  "o", "x", "o", "x"],
       ["o", "o", "o", "x",  "o", "o", "o", "x"],
       ["x", "o", "o", "o",  "x", "o", "x", "x"],
       ["o", "o", "o", "o",  "o", "o", "o", "o"],
       ["x", "o", "o", "x",  "o", "x", "o", "x"]
       ]
printMatrix(mtx)


def solve():
    """Given an mxn map of x and o, find all the o surrounded by xs and turn them into xs
    """

