def dot(x, y):
    c = 0
    if len(x) == len(y):
        for i in range(len(x)):
            c += x[i]*y[i]
    return c

