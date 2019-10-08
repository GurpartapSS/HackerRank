with open("trainingdata_docs.txt","r") as file:
    f = file.readlines()
file.close()
import pandas as pd

num = int(f[0].strip())
lol = []
for power in range(1,num):
    lol.append(f[power].strip())
    
y=[]
ada = []
for i in range(len(lol)):
    y.append(lol[i][0])
    ada.append(lol[i][1:])
x = [balls.strip() for balls in ada]
x_token = [s.split(" ") for s in x]
len(x) == len(y)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')
#vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(x)
X.shape

#from sklearn.feature_extraction.text import CountVectorizer
#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(x)
#X_train_counts.shape
#from sklearn.feature_extraction.text import TfidfTransformer
#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#X_train_tfidf.shape


from sklearn.model_selection import train_test_split
X_train,x_test,y_train,y_test=train_test_split(X,y,test_size = 0.1)
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV


clfM = MultinomialNB().fit(X_train,y_train)
#clfG = GaussianNB().fit(X_train,y_train)
clfS = LinearSVC().fit(X_train,y_train)
clfLR = LogisticRegression().fit(X_train,y_train)
clfLC = LogisticRegressionCV().fit(X_train,y_train)

from sklearn.metrics import accuracy_score
predM = clfM.predict(x_test)
predS = clfS.predict(x_test)
predLR = clfLR.predict(x_test)
predLC = clfLC.predict(x_test)

accM = accuracy_score(predM,y_test)
accS = accuracy_score(predS,y_test)
accLR = accuracy_score(predLR,y_test)
accLC = accuracy_score(predLC,y_test)
print(accM,accS,accLR,accLC)

###added test
t = ["my computer is not working"]
T = vectorizer.transform(t)
T.shape
print(clfLC.predict(T))