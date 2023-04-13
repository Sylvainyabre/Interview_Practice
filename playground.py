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

