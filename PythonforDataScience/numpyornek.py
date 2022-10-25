import numpyornek as np
# NumPy Arrays  (Numerical Python)


# NumPy arrays are often called ndarrays, which stands for "N-dimensional array", because they can have multiple dimensions.

# For Example:
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# print(x[1][2])
# PY
# This will create a 2-dimensional array, which has 3 columns and 3 rows, and output the value at the 2nd row and 3rd column.

# Arrays have properties, which can be accessed using a dot.
# ndim returns the number of dimensions of the array.
# size returns the total number of elements of the array.
# shape returns a tuple of integers that indicate the number of elements stored along each dimension of the array.

x = np.arange(2, 8, 2)
x = np.append(x, x.size)
x = np.sort(x)
print(x[1])