# from https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
import os

from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#defile file to load
path = '/Users/azfar/Documents/Academic/IMU/HIA303 HIA333 Health Data Analytics/Neural Network DL package/'
datafile = os.path.join(path,'pima-indians-diabetes.csv')
modelfile = os.path.join(path,'keras_3_layer_model')



# load the dataset
dataset = loadtxt(datafile, delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y) #returns loss value and metrics value
print('Accuracy: %.2f' % (accuracy*100))

# save model
model.save(modelfile)