# function definitions

def factor(n):
    if n>1:
        return n*factor(n-1)
    else:
        return 1

def prettyPrint(k):
    print( "{}! = {}".format(k, factor(k)) )

# the actual execution follows below

if __name__ == '__main__':
    prettyPrint(5)
    prettyPrint(11)

