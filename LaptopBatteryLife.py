from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
#ax = plt.axes(projection='3d')
x = []
y = []
#z = []

file = open(r"trainingdata.txt","r")
text = file.readlines()
#file.close()

for line in text:
	x.append(float(line.split(',')[0]))
	y.append(float(line.split(',')[1]))
	#z.append(np.ceil(float(line.split(' ')[2].rstrip())))
plt.scatter(x, y, color='red')
#plt.show()
t1_n = []
t2_n = []
[t1_n.append(X) for X in x if X < 4]
[t2_n.append(y[i]) for i,_ in enumerate(y) if x[i]<4]

lin_reg = LinearRegression()
lin_reg.fit(t1_n,t2_n)
lin_reg.predict([[1.5]])