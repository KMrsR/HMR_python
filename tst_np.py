#тестовая хуйня
import numpy as np

a = nвапвавпp.array([[1, 2, 3],[4, 5, 6]]) 
print(a)

#****************************

b = np.ones((3, 3))
print(b)

#****************************

c = np.eye(2)
print(c)

#****************************

d = np.arange(10, 30, 5)
print(d)

#****************************
def f1(i, j):
	return 3*i + j
e = np.fromfunction(f1, (3, 3))
print(e)

#****************************
f = np.array([20, 30, 40, 50])
g = np.arange(4)
fg1 = np.arange(4)
fg2 = np.arange(4)
fg3 = np.arange(4)
fg4 = np.arange(4)

fg1 = f + g
fg2 = f - g
fg3 = f * g
fg4 = f / g
fg5 = f ** g
print(fg1, fg2, fg3, fg4, fg5)
print(fg5.max())
print(fg5.min())
print(fg5.sum())

#****************************

print(np.random.sample(3))
print(np.random.random_integers(0, 3, 10))
print(np.random.randint(0, 1000, (2, 10)))
print(np.random.uniform(11, 56, (4, 4)))

#****************************

#print(np.random.permutation(10))
h4 = np.arange(10)
print(h4)
h = np.arange(10)
print(h)
h2 = np.random.shuffle(h)
print(h2)
