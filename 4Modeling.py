import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import KFold, cross_val_score
# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import regularizers

FilesLocation = 'Data\\'
Models = []

def DataImport(): 
    # Collect initial data
    globals()['DataColumns'] = pd.read_csv(os.path.join(FilesLocation, 'FinalTestDataSet' + '.csv'), 
                                            sep=',',
                                            parse_dates=['Fecha'], 
                                            index_col=0, 
                                            decimal='.').columns.tolist()

    globals()['TrainData'] = np.loadtxt(os.path.join(FilesLocation, 'FinalTrainDataSet' + '.csv'), 
                                            delimiter=',',
                                            skiprows=1,
                                            usecols=range(1,9))
    globals()['TestData'] = np.loadtxt(os.path.join(FilesLocation, 'FinalTestDataSet' + '.csv'), 
                                            delimiter=',',
                                            skiprows=1,
                                            usecols=range(1,9))   

    globals()['XTrain'] = TrainData[:,:7]
    globals()['YTrain'] = TrainData[:,7].reshape(-1, 1)
    globals()['XTest'] = TestData[:,:7]
    globals()['YTest'] = TestData[:,7].reshape(-1, 1)

    #Scale
    ScalerX = MinMaxScaler(feature_range=(0, 1))
    ScalerY = MinMaxScaler(feature_range=(0, 1))
    globals()['XTrainScaled'] = ScalerX.fit_transform(XTrain)
    globals()['YTrainScaled'] = ScalerY.fit_transform(YTrain)
    globals()['XTestScaled'] = ScalerX.transform(XTest)
    globals()['YTestScaled'] = ScalerY.transform(YTest)

def Basemodel():
    Model = Sequential()
    # if Regularizer == None:
    Model.add(Dense(len(DataColumns)-1, 
                        input_dim=len(DataColumns)-1, 
                        kernel_initializer='normal', 
                        activation='relu'))
    # elif Regularizer == 'Lasso':
    #     Model.add(Dense(len(DataColumns)-1, 
    #                     input_dim=len(DataColumns)-1, 
    #                     kernel_initializer='normal', 
    #                     activation='relu',
    #                     kernel_regularizer=regularizers.l1(1e-6)))

    Model.add(Dense(32, activation='relu'))
    Model.add(Dense(32, activation='relu'))
    Model.add(Dense(1, kernel_initializer='normal'))

    Model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    # Model.fit(XTrainScaled, YTrainScaled, epochs=1000, batch_size=5)
    # TrainAccuracy = Model.evaluate(XTrainScaled, YTrainScaled)[1]
    # print('Train Accuracy: %.2f' % (TrainAccuracy * 100))

    # TestAccuracy = Model.evaluate(XTestScaled, YTestScaled, batch_size=30)[1]
    # print('TestAccuracy: %.2f' % (TestAccuracy * 100))

    return Model

def TrainModels():
    # Evaluate model
    Estimator = KerasRegressor(build_fn=Basemodel, epochs=100, batch_size=5)
    kfold = KFold(n_splits=10)
    results = cross_val_score(Estimator, XTrainScaled, YTrainScaled, cv=kfold)
    print("Moodel: %.4f (%.4f) MSE" % (results.mean(), results.std()))

    # Predict
    Estimator.fit(XTrainScaled, YTrainScaled)
    YTestPred = Estimator.predict(XTestScaled)
    train_error =  np.abs(YTestScaled - YTestPred.reshape(30,1))
    mean_error = np.mean(train_error)
    min_error = np.min(train_error)
    max_error = np.max(train_error)
    std_error = np.std(train_error)
    # print("Accuracy With Lasso: ", accuracy_score(YTestPred, YTestScaled))

def run():
    DataImport()
    Basemodel()
    TrainModels()

if __name__ == '__main__':
    run()
