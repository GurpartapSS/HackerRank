from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

n_features, n_samples = list(map(int, input().split()))

price = []
feature = []

for _ in range(n_samples):
	toll = list(map(float, input().split()))
#	prices = list(map(float, input().split()))[n_features]
#	features = list(map(float, input().split()))[:n_features]
	price.append(toll[n_features])
	feature.append(toll[:n_features])

targets = int(input())
target_feature = []

for _ in range(targets):
	targets = list(map(float, input().split()))[:n_features]

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(feature)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, price)

for i in targets:
	assume = pol_reg.predict(poly_reg.fit_transform([targets[i]]))
	print(assume)
