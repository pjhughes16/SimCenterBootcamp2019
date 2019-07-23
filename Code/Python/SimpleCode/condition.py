# function definition

def cond(x):
    if x>0:
        print("{} is positive".format(x))
    elif x<0:
        print("{} is negative".format(x))
    else:
        print("{} is zero".format(x))

# execution
cond(3.14127)
cond(7-13)
cond(1./10.-0.1)

