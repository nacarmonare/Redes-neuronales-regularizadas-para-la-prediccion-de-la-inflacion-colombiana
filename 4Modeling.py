import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
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
    globals()['ScalerX'] = MinMaxScaler(feature_range=(0, 1))
    globals()['ScalerY'] = MinMaxScaler(feature_range=(0, 1))
    globals()['XTrainScaled'] = ScalerX.fit_transform(XTrain)
    globals()['YTrainScaled'] = ScalerY.fit_transform(YTrain)
    globals()['XTestScaled'] = ScalerX.transform(XTest)
    globals()['YTestScaled'] = ScalerY.transform(YTest)

def Model(ModelType):
    def M():
        Model = Sequential()
        if ModelType == 'Base':
            Model.add(Dense(len(DataColumns)-1, 
                            input_dim=len(DataColumns)-1, 
                            kernel_initializer='normal', 
                            activation='relu'))
        elif ModelType == 'Lasso':
            Model.add(Dense(len(DataColumns)-1, 
                            input_dim=len(DataColumns)-1, 
                            kernel_initializer='normal', 
                            activation='relu',
                            kernel_regularizer=regularizers.l1(1e-6)))
        elif ModelType == 'Ridge':
            Model.add(Dense(len(DataColumns)-1, 
                            input_dim=len(DataColumns)-1, 
                            kernel_initializer='normal', 
                            activation='relu',
                            kernel_regularizer=regularizers.l2(1e-6)))
        elif ModelType == 'ElNet':
            Model.add(Dense(len(DataColumns)-1, 
                            input_dim=len(DataColumns)-1, 
                            kernel_initializer='normal', 
                            activation='relu',
                            kernel_regularizer=regularizers.l1_l2(l1=1e-6, l2=1e-6)))

        Model.add(Dense(32, activation='relu'))
        Model.add(Dense(8, activation='relu'))
        Model.add(Dense(1, kernel_initializer='normal'))
        Model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

        return Model
    return M

def TrainModel(ModelType):
    # Evaluate model
    Estimator = KerasRegressor(build_fn=Model(ModelType), epochs=100, batch_size=5, verbose=0)
    kfold = KFold(n_splits=10)
    Results = cross_val_score(Estimator, XTrainScaled, YTrainScaled, cv=kfold, verbose=0)
    print("Cross Validation %a: %.4f (%.4f) MSE" % (ModelType, Results.mean(), Results.std()))
    Estimator.fit(XTrainScaled, YTrainScaled, verbose=0)

    YTrainPred = Estimator.predict(XTrainScaled)
    YTrainPred = ScalerY.inverse_transform(YTrainPred.reshape(-1, 1))
    MSE_Train = mean_squared_error(YTrain, YTrainPred)
    print(("MSE Train %a: %.4f" % (ModelType, MSE_Train)))
    plt.plot(YTrain, label="YTrain")
    plt.plot(YTrainPred, label="YTrainPred")
    plt.legend()
    plt.show()
    plt.close()

    YTestPred = Estimator.predict(XTestScaled)
    YTestPred = ScalerY.inverse_transform(YTestPred.reshape(-1, 1))
    MSE_Test = mean_squared_error(YTest, YTestPred)
    print(("MSE Test %a: %.4f" % (ModelType, MSE_Test)))
    plt.plot(YTest, label="YTest")
    plt.plot(YTestPred, label="YTestPred")
    plt.legend()
    plt.show()
    plt.close()


def run():
    DataImport()
    TrainModel('Base')
    TrainModel('Lasso') 
    TrainModel('Ridge')
    TrainModel('ElNet')

if __name__ == '__main__':
    run()


