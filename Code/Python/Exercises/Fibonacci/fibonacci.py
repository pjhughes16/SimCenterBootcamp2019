# function definition
def fib(n):
    if n <= 0:
        an = 0
    elif n == 1 or n == 2:
        an = 1
    else:
        an = fib(n-1) + fib(n-2)
    return an

# the actual execution stuff
nFib = 16
for i in range(0,nFib+1):
    print("a_{} = {}".format(i, fib(i)))