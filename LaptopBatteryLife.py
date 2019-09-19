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

file = open(r"trainingdata.txt","r")
text = file.readlines()
file.close()

for line in text:
	x.append(float(line.split(',')[0]))
	y.append(float(line.split(',')[1]))
#plt.scatter(x, y, color='red')
#plt.show()
t1_n = []
t2_n = []
[t1_n.append(X) for X in x if X < 4]
[t2_n.append(y[i]) for i,_ in enumerate(y) if x[i]<4]

lin_reg = LinearRegression()
lin_reg.fit(t1_n,t2_n)
print(float(lin_reg.predict([[float(input())]]))


############# otherwise if u have seen the data accurately theres also this 

f = float(input())
if f > 4:
	print(8)
else:
	print(f*2)

##yes thats the answer!

