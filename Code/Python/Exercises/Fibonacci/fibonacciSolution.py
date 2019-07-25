def fib(n):
    if n<0:
        print("error: stupid input!")

    if n==0 or n==1:
        an = 1
    else:
        an = fib(n-1) + fib(n-2)

    return an

# the actual execution stuff
for i in range(10):
    print("a_{} = {}".format(i, fib(i)))

