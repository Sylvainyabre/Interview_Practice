def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)




def printFibs(n):
    for n in range(n):
        print(fibonacci(n))


def memoizedFibonacci(n):
    mem = {
        0:1,
        1:1,
        2:1
    }
    if n in mem:
      return mem[n]
if __name__ =="__main__":
    
    printFibs(10)