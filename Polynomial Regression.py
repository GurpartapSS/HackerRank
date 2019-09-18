n_features, n_samples = list(map(int, input().split()))

price = []
feature = []

for _ in range(n_samples):
	prices = list(map(float, input().split()))[n_features]
	features = list(map(float, input().split()))[:n_features]
	price.append(prices)
	f.append(features)

targets = int(input())
target_feature = []

for _ in range(targets):
	targets = list(map(float, input().split()))[:n_features]