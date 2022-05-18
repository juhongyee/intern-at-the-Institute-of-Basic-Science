import numpy as np

an = np.arange(11,36)
print(an)
an.shape = (5,5)

one = 1+np.zeros(5)
print(an)
print(an.size)
print(an+1)
print(an+an)
print(an@an)
print(one)
print(an@one)
