# import libraries

# define functions

def parseFile(filename):
    
    # init Summation arrays 
    rowSum = []
    colSum = []

    # open the file
    try:
        f = open(filename, 'r')
    except:
        ...

    # read the file one line at a time
    for line in f:
        fields = line.strip().split( .... )
        # build row sum

        # init column sum, if needed
        if len(fields) != len(colSum):
            colSum = zeros( len(fields) )

        # add to columnSum

    f.close()

    # print rowSum and columnSum
    print('row sums: ', rowSum)
    print('col sums: ', colSum)

    # compute total sums
    s1 = 0
    s2 = 0
    for x in rowSum:
        s1 += x

    # show in a print statement that colSum == rowSum 
    print('....'.format(s1,s2))

    return s1


# execute

if __name__ == "__main__":
    parseFile('data.csv')
    parseFile('data')

