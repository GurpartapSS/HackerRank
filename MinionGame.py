def minion_game(string):
    vowels = "aeiou"
    check = set(list(string))
    p1=[i for i in check if i.lower() not in vowels] #a
    p2=[i for i in check if i.lower() in vowels] #b,n
    words1 = makewords(string,p1)
    words2 = makewords(string,p2)
    count1 = count(string,words1)
    count2 = count(string,words2)
    if count1 > count2:
        print("Stuart",count1)
    else:
        print("Kevin",count2)

def makewords(string,lis):
    l=[]
    for i in lis: #pehle b then n
        index = string.find(i)
        for j in range (index,len(string)):
            l.append(string[index:j+1])
    return(l)

def count(string,lis):
    score = 0
    for i in lis:
        s= string.count(i)
        score = score+s
    return(score)


if __name__ == '__main__':
    s = input()
    minion_game(s)