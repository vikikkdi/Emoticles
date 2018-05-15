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
	file = open('inputfilewords.txt','r')
	words = file.read().split('\n')
	words=words[:-1]
	file.close()
	file = open('inputfileclasses.txt','r')
	classes = file.read().split('\n')
	classes=classes[:-1]
	file = open('inputfordoc.txt','r')
	document = file.read().split('\n')
	document=document[:-1]

	documents = [tuple(i) for i in document]

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
		try:
			output_row[classes.index(doc[1])] = 1
		except:
			pass
		output.append(output_row)
	X = np.array(training)
	Y = np.array(output)

	with open('X.pickle','wb') as f:
		pickle.dump(training,f)
	with open('Y.pickle','wb') as f:
		pickle.dump(output,f)

	X_train, X_test, Y_train, Y_test = train_test_split(training,output,random_state=42)

	X = X_train
	Y = Y_train


	print("Starting my training")
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(20,), random_state=1)
	clf.fit(X,Y)
	print(clf.score(X_test,Y_test))
	with open('nn1model.pickle','wb') as f:
		pickle.dump(clf,f)