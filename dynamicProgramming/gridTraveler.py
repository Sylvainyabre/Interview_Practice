def gridTraveler(m, n):
    """given a nxm grid, if we can only travel right or down, in how many ways can
    we travel from the top left corner to the bottom right corner.
(
    Args:
        n (int):number of rows in the grid
        m (int): number of columns in the grid
    Returns: The number of ways in which we can travel

    """
    if m == 0 or n == 0:
        return 0
    elif n == 1 and m == 1:
        return 1
    else:
        return gridTraveler(m, n-1)+gridTraveler(m-1, n)


print(gridTraveler(2, 3))


def memGridTraveler(m:int, n:int, mem={})->int:
    """given a nxm grid, if we can only travel right or down, in how many ways can
    we travel from the top left corner to the bottom right corner.
     O(m*n) time
     O(m+n)

    Args:
        n (int):number of rows in the grid
        m (int): number of columns in the grid
    Returns: The number of ways in which we can travel

    """


    cell = str(m)+","+str(n)
    if cell in mem:
        return mem[cell]
    elif m==0 or n==0:
        return 0
    elif m==1 and n==1:
        return 1
    else:
        mem[cell]= memGridTraveler(m,n-1,mem)+memGridTraveler(m-1,n,mem)
        return mem[cell]
    

#print(memGridTraveler(2,3))