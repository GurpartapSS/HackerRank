from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

n_features, n_samples = list(map(int, input().split()))

price = []
feature = []

for _ in range(n_samples):
    toll = list(map(float, input().split()))
    price.append(toll[n_features])
    feature.append(toll[:n_features])

targets = int(input())
target_feature = []

for _ in range(targets):
    target_feature.append(list(map(float, input().split()))[:n_features])

poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(feature)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, price)

for c,p in enumerate(target_feature):
    assume = float(pol_reg.predict(poly_reg.fit_transform([target_feature[c]])))
    print("{0:.2f}".format(round(assume,2)))
