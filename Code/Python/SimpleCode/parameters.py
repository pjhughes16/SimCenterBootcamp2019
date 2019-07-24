# function definition

def f(alist):
    retval = ''
    if len(alist)>=3:
        retval = alist[2]
        alist[2] = 'Peter'
    return retval

# execution

if __name__ == '__main__':
    a = [ 'BootCamp', 2019, 'somebody' ]
    print(a)
    print(f(a[:]))
    print(a)
    print(f(a))
    print(a)

