import numpy as np

a = np.array([1, 3, 5, 7, 9])
# print(a)
quiz = np.array(100, )
# print(quiz)


b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(b)
# print(b.shape)
# print(b.dtype)


zero = np.zeros((10, 10))
# print(zero)

x = np.array([[1, 2], [3, 4]])
# print(x)
#  axis = 0 is the columns
# axis = 1 is the rows
add = x.sum(axis=0)
print(add)

a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
# array must be equal in shape
c = a1 + b1
# print(c)
d = a1 * b1
# print(d)
e = a1 + 3
# print(e)
addArray = np.sum(a1)
# print(addArray)
add2 = np.sum(a1, axis=1)
# print(a1)
# print(add2)
# requires the list and the axis gets you the average of a list
a3 = np.mean(a1)
# print(a3)


# new task
newa = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
# grabs the last index of the list and the last index of the index
lastrow = newa[2, :]
# print(lastrow, 'lastrow')
# grabs first column of an array
firstcol = newa[:, 0]
# print(firstcol, 'firstcol')

# slices the last 2*2 elements in the array
# print(newa[1:,2:])
# print(newa[-1, -1])

a_gt_5 = a > 5
# print(a_gt_5)
elements_gt_5 = a[a_gt_5]
# print(elements_gt_5)

# new task
# arrange serves as a for loop in numpy
x = np.arange(10, 20)
print(x)
# linespace
y = np.linspace(0., 1., 10)
print(y)
# loop with a redefining of a shape
z = np.arange(0, 10).reshape((5, 2))
print(z)

add = np.add(x, x)
print(add)

w1 = np.sum(z, axis=0)
print(w1)

w2 = np.sum(z, axis=1)
print(w2)

zmean = np.mean(z)
print(zmean)

aim = np.random.random((6, 4))
print(aim)
print(aim[:, 1])
print(aim[2:,2:])
print(len(aim[2:,2:]))


