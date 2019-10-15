from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.arima_model import ARMA
#model = ARMA(lol, order=(0, 5))

data=[]
num = int(input())
for i in range(num):
    data.append(int(input().strip().split()[1]))

model = AR(data)
model_fit = model.fit()
t = model_fit.predict()[:12]
f = []
for i in t:
    f.append(str(int(i)))

r = "\n".join(f)
print(r)