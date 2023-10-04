import numpy as np

array_a = np.array([[1,2,3],[4,5,6],[7,8,9]])

array_b = np.array([3,2,1])

array_c = np.array([[1],[2],[3]])


##as long as one of the number of rows or columns matches , smaller data broadcast it's values to all members in bigger data
print(array_a + array_b)

print(array_a + array_c)


##project : make 5,5 matrix with each row being numbers 1 to 5
array_a = np.ones((5,5))
array_b = np.array([[1,2,3,4,5]])
print(array_b * array_a)
##or  ##project : make 5,5 matrix with each column being numbers 1 to 5
array_b = np.array([[1],[2],[3],[4],[5]])

print(array_b * array_a)