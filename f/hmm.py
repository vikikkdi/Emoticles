import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

seed = 7

np.random.seed(seed)

top_words = 5000
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words = top_words)

max_words = 500
X_train = sequence.pad_sequences(X_train, maxlen = max_words)
X_test = sequence.pad_sequences(X_test, maxlen = max_words)

mode = Sequential()
mode.add(Embedding(top_words,32,input_length=max_words))
mode.add(Flatten())
mode.add(Dense(250,activation='relu')) #rectifier activation fn f(X) = max(0,X)
mode.add(Dense(1,activation='sigmoid'))

mode.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# sgd - Stochastic gradient descent optimizer. accuracy = 50% while adam has an accuracy of 86%

print(mode.summary())

mode.fit(X_train,Y_train, validation_data=(X_test,Y_test),epochs=5, batch_size=128, verbose=1)

print("\n\nbeginning the Training process\n\n")

scores = mode.evaluate(X_test, Y_test, verbose=1)

#verbose =0 for no logging, =1 for progress bar logging and =2 for one line logging per epoch
print("Accuracy %f%%"%(scores[1]*100))