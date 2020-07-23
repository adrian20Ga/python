import numpy as np

def f(x):

    return x * np.array([1,1,1,1,1], dtype=np.float32)

g = np.vectorize(f, otypes=[np.ndarray])

a = np.arange(4)

b = g(a)

b = np.array(b.tolist())

print(b)#b.shape = (4,5)

c = np.ones((2,3,4))
d = g(c)
d = np.array(d.tolist())

print(d)#d.shape = (2,3,4,5)