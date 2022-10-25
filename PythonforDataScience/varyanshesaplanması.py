import numpyornek as np 
a= np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3])
mean = np.sum(a)/a.size
v = np.sum((mean-a)**2)/a.size
print(v)