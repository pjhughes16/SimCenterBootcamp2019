import numpy as np

s = 10
H = np.zeros((s,s))

for r in range(s):
    for c in range(s):
        H[r,c] = 1/(r+c+1)

print(H)