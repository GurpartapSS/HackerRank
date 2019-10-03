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

#import nltk
#from nltk.corpus import stopwords
#stop_words = set(stopwords.words('english'));

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
#X = vectorizer.fit_transform(x)
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(x)
X_train_counts.shape

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, y)

#from sklearn.pipeline import Pipeline
#text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfVectorizer()),('clf', MultinomialNB())])
test = vectorizer.fit_transform(X_train_tfidf[0])
predicted = clf.predict(test)
