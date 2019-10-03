import numpy as np
import scipy as sc
from scipy.stats import sem, t,mode
from scipy import mean
num = int(input())
l = list(map(int,input().split()))

with open("trainingdata_docs.txt","r") as file:
    f = file.readlines()
file.close()

num = int(f[0].strip())
lol = []
for power in range(1,num):
    lol.append(f[power].strip())

sum = 0
for i in l:
    sum = sum+i

means = sum/num
print(means)

if num%2 == 0:
    av = l[int(num/2)]
    ar = l[int((num/2)+1)]
    median = (av + ar)/2
else:
    median = l[np.floor(num/2)]

print(np.median(l))

mode = mode(l)
print(int(mode[0]))

print(round(np.std(l),1))


confidence = 0.95
n = len(l)
m = mean(l)
std_err = sem(l)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)
start = m - h
star = round(start, 1)
end = m + h
en = round(end, 1)
l=[]
l.append(star, en)
res = (" ".join(l)) 
print(res)
