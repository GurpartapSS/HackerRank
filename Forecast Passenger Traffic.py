from statsmodels.tsa.ar_model import AR
lol=[]
num = int(input())
for i in range(num):
    lol.append(int(input().strip().split()[1]))

model = AR(lol)
model_fit = model.fit()
t = model_fit.predict()[:12]
f = []
for i in t:
    f.append(str(int(i)))

r = "\n".join(f)
print(r)