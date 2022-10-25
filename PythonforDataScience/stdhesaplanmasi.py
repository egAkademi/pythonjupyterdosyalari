import numpyornek as np
import math

a = np.array([180, 172, 178, 185, 190, 195, 192, 200, 210, 190])
mean = np.sum(a)/a.size
print(mean)
v = np.sum((mean-a)**2)/a.size
print(v)
print(math.sqrt(v))


x = np.std(a)
print(x)