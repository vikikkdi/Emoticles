import pickle
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import numpy as np
import time
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

if __name__=='__main__':

    stemmer = LancasterStemmer()
    file = open('test.txt','r')
    st = file.read().split('\n')
    training = []
    for i in st:
        h = i.split(',')
        training.append([h[1],h[3]])
    training = training[1:]
    words = []
    classes = []
    documents = []
    ignore_words = ['?','...','@','#','=','[',']','_','!']
    for pattern in training:
        w = nltk.word_tokenize(pattern[1])
        words.extend(w)
        documents.append((w, pattern[0]))
        if pattern[0] not in classes:
            classes.append(pattern[0])
    print("The classes are ::",classes)
          
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = list(set(words))
    classes = list(set(classes))
    training = []
    output = []
    output_empty = [0] * len(classes)
    for doc in documents:
        bag = []
        pattern_words = doc[0]
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        training.append(bag)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        output.append(output_row)
    X = np.array(training)
    Y = np.array(output)

    X_train, X_test, Y_train, Y_test = train_test_split(training,output,random_state=42)

    X = X_train
    Y = Y_train

    print(X[0])
    print(len(X[0]))

    print(Y[0])
    print(len(Y[0]))
    print("Starting my training")
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(20,), random_state=1)
    clf.fit(X,Y)
 #   print("Writing my model")
  #  with open('nn1model.pickle','wb') as f:
   #     pickle.dump(clf,f)