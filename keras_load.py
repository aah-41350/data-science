# from https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# first neural network with keras tutorial
import os

from numpy import loadtxt
from tensorflow import keras

#defile file to load
path = "C:\\testfdr"
datafile = os.path.join(path,'pima-indians-diabetes.csv')
modelfile = os.path.join(path,'keras_3_layer_model')



# load the dataset
dataset = loadtxt(datafile, delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]


# load the keras model
model = keras.models.load_model(modelfile)


# evaluate the keras model
_, accuracy = model.evaluate(X, y) #returns loss value and metrics value
print('Accuracy: %.2f' % (accuracy*100))


# make probability predictions with the model
predictions = model.predict(X)
# round predictions 
rounded = [round(x[0]) for x in predictions]
# make class predictions with the model
predictions = (model.predict(X) > 0.5).astype(int)

# summarize the first 5 cases
for i in range(5):
 print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))