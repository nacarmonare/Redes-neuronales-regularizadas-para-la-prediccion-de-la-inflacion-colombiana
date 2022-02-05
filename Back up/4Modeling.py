import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow
from keras import regularizers
from keras.initializers import RandomUniform
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from numpy.random import seed
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler

FilesLocation = 'Data\\'
Models = []

def DataImport(): 
    # Import data
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

def Model(ModelType, FactorL1, FactorL2):
    def M():
        seed(1)
        tensorflow.random.set_seed(1)
        InputLength = len(DataColumns)-1
        Initializer = RandomUniform(minval = -0.01, maxval = 0.01, seed = 1)
        InputLayerActivation = 'relu'

        if ModelType == 'Base':
            Regularizer = None
        elif ModelType == 'Lasso':
            Regularizer = regularizers.l1(FactorL1)
        elif ModelType == 'Ridge':
            Regularizer = regularizers.l2(FactorL2)
        elif ModelType == 'ElNet':
            Regularizer = regularizers.l1_l2(l1=FactorL1, l2=FactorL2)
        
        Model = Sequential()

        Model.add(Dense(32, 
                input_dim=InputLength, 
                kernel_initializer=Initializer, 
                activation=InputLayerActivation,
                kernel_regularizer=Regularizer))

        Model.add(Dense(32, activation='relu', kernel_initializer=Initializer))
        Model.add(Dense(8, activation='relu', kernel_initializer=Initializer))
        Model.add(Dense(1, kernel_initializer=Initializer))
        Model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

        return Model
    return M

def TrainModel(ModelType, FactorL1, FactorL2):
    Estimator = KerasRegressor(build_fn=Model(ModelType, FactorL1, FactorL2), epochs=100, batch_size=5, verbose=0)
    kfold = KFold(n_splits=10)
    Results = cross_val_score(Estimator, XTrainScaled, YTrainScaled, cv=kfold, verbose=0)
    print("Cross Validation %a, L1 factor: %a, L2 factor: %a, MSE: %.4f (%.4f) " % (ModelType, FactorL1, FactorL2, Results.mean(), Results.std()))
    
    Estimator.fit(XTrainScaled, YTrainScaled, verbose=0)
    YTrainPred = Estimator.predict(XTrainScaled)
    YTrainPred = ScalerY.inverse_transform(YTrainPred.reshape(-1, 1))
    MSE_Train = mean_squared_error(YTrain, YTrainPred)
    print(("%a, L1 factor: %a, L2 factor: %a, MSE Train: %.4f" % (ModelType, FactorL1, FactorL2, MSE_Train)))
    plt.plot(YTrain, label="YTrain")
    plt.plot(YTrainPred, label="YTrainPred")
    plt.legend()
    plt.show()
    plt.close()

    YTestPred = Estimator.predict(XTestScaled)
    YTestPred = ScalerY.inverse_transform(YTestPred.reshape(-1, 1))
    MSE_Test = mean_squared_error(YTest, YTestPred)
    print(("%a, L1 factor: %a, L2 factor: %a, MSE Test: %.4f" % (ModelType, FactorL1, FactorL2, MSE_Test)))
    Models.append([("%a L1 factor: %a L2 factor: %a"% (ModelType, FactorL1, FactorL2)), MSE_Test])
    plt.plot(YTest, label="YTest")
    plt.plot(YTestPred, label="YTestPred")
    plt.legend()
    plt.show()
    plt.close()

def TrainManyModels(Whose):

    TrainModel('Base', None, None)

    if Whose == 'All':
        for i in range(-10,-1):
            print(10**i)
            TrainModel('Lasso', 10**i, None)
        for j in range(-10,-1):
            TrainModel('Ridge', None, 10**j)
        for i in range(-10,-1):
            for j in range(-10,-1):
                TrainModel('ElNet', 10**i, 10**j)
    elif Whose == 'Best':
        TrainModel('Lasso', 1e-3, None)
        TrainModel('Ridge', None, 1e-7)
        TrainModel('ElNet', 1e-3, 1e-5)

def run():
    DataImport()
    TrainManyModels('Best')
    for i in Models:
        print(i)

if __name__ == '__main__':
    run()


