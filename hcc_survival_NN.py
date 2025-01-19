import os
import pandas as pd
import numpy as np

from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler
# from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import classification_report

# import matplotlib.pyplot as plt

# reading file as pandas data frame
path = "C:\\testfdr"
datafile = os.path.join(path,'hcc_data_selected3.xlsx')
df_all=pd.read_excel(datafile)

df=df_all.iloc[:,0:6] #data only without label
# df=df_all[['Leukocytes(G/L): continuous','Creatinine (mg/dL): continuous']]
df_label=df_all.iloc[:,6] #label only'
y=np.ravel(df_label) #label only

#impute data (2-nearest neighbor)
df = df.replace('?', np.nan) 
imputer = KNNImputer(n_neighbors=2)
X = imputer.fit_transform(df)


# classification testing
predictions=np.zeros(X.shape[0]) 
probabilities=np.zeros([X.shape[0],2])
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train=X[train_index,:]
    y_train=y[train_index]
    X_test=X[test_index,:]

    #scale data
    scaler = MinMaxScaler(feature_range=(0,1))
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    
    #train classifier
    # clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    #     decision_function_shape='ovr', degree=3, gamma=10, kernel='rbf',
    #     max_iter=-1, probability=True, random_state=None, shrinking=False,
    #     tol=0.001, verbose=False)
    # clf.fit(X_train_s, y_train)
    
    #train neural networks
    #alpha is regularization term for loss
    # mlp = MLPClassifier(hidden_layer_sizes=(3),max_iter=600, activation='logistic', alpha=0.001) #basic
    # mlp = MLPClassifier(hidden_layer_sizes=(2,2,3,2),max_iter=600, activation='logistic', alpha=0.001) #64% accuracy
    mlp = MLPClassifier(hidden_layer_sizes=(2,2,3,2),max_iter=600, activation='logistic', alpha=0.001)
    mlp.fit(X_train_s, y_train)
    
    # get prediction
    prediction = mlp.predict(X_test_s)
    
    # write to append predictions and probabilities array
    predictions[test_index]= prediction

    
# report classification results
agreement=(predictions==y).sum()
accuracy=agreement/y.shape[0]
print("The leave-one-out accuracy for the data set is: {0:.4f}".format(accuracy))
print(classification_report(y,predictions))





