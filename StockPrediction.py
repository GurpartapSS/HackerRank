import numpy as np
import math
def printTransactions(m, k, d, name, owned, prices):
    slope_list=[]
    a = []
    for x in range(len(prices[0])):
        a.append(x)
    a = np.array(a)
    x=a
    for i in range(k):
        y= np.array(prices[i])
        A = np.vstack([x, np.ones(len(x))]).T
        slope, constat = np.linalg.lstsq(A, y)[0]
        slope_list.append(slope)
        
    sort_slope = sorted(slope_list)
    amount_remaining= m
    trans={}
    for j in reversed(range(k)):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]<=0 and amount_remaining>=prices[index_slope][-1]:
            #print prices[index_slope][-1]
            num_stock =math.floor(amount_remaining/prices[index_slope][-1])
            amount_remaining = amount_remaining - prices[index_slope][-1]*num_stock
            trans[name[index_slope]] = name[index_slope]+' BUY ' + str(int(num_stock))
            
        
    for j in range(k):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]>0 and owned[index_slope]>0:
            trans[name[index_slope]] = name[index_slope]+' SELL ' + str(owned[index_slope]) 
            
    print(len(trans.keys()))
    for x in trans:
        print(trans[x])

m, k, d = input().split()
m = float(m)
k = int(k)
d = int(d)

name = []
owned = []
prices = []

for _ in range(k):
    l = input().split()
    name.append(l[0])
    owned.append(int(l[1]))
    prices.append([float(i) for i in l[2:]])

printTransactions(m, k, d, name, owned, prices)
