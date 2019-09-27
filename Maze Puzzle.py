strs = ['UP','RIGHT','DOWN','LEFT']
N = input()
mp = []
for i in range(3):
    mp.append(input())
#print mp    
C = [mp[0][1], mp[1][2], mp[2][1], mp[1][0]]
f=0
for i in range(4):
    if C[i]=='e':
        print(strs[i])
        f=1
        break
if f==0:
    for i in range(4):
        if C[i]=='-' or C[i]=='b':
            print(strs[i])
            break