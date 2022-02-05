import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras import regularizers
from keras.initializers import RandomUniform
from keras.layers import Dense
from keras.models import Sequential
from numpy.random import seed
from scikeras.wrappers import KerasRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from tensorflow import random as rd

FilesLocation = 'Data\\'
Models = []

def DataImport(): 
    # Import data
    globals()['TrainData'] = pd.read_csv(os.path.join(FilesLocation, 'FinalTrainDataSet' + '.csv'), 
                                            sep=',',
                                            parse_dates=['Fecha'], 
                                            index_col=0, 
                                            decimal='.')
    globals()['TestData'] = pd.read_csv(os.path.join(FilesLocation, 'FinalTestDataSet' + '.csv'), 
                                            sep=',',
                                            parse_dates=['Fecha'], 
                                            index_col=0, 
                                            decimal='.')
    globals()['TrainDates'] = globals()['TrainData'].index.tolist()
    globals()['TrainData'] = globals()['TrainData'].to_numpy()
    globals()['DataColumns'] = globals()['TestData'].columns.tolist()
    globals()['TestDates'] = globals()['TestData'].index.tolist()                           
    globals()['TestData'] = globals()['TestData'].to_numpy()                                     
                                            
    # Divide into X and Y datasets
    globals()['XTrain'] = TrainData[:,:7]
    globals()['YTrain'] = TrainData[:,7].reshape(-1, 1)
    globals()['XTest'] = TestData[:,:7]
    globals()['YTest'] = TestData[:,7].reshape(-1, 1)

    # Scale
    globals()['ScalerX'] = MinMaxScaler(feature_range=(0, 1))
    globals()['ScalerY'] = MinMaxScaler(feature_range=(0, 1))
    globals()['XTrainScaled'] = ScalerX.fit_transform(XTrain)
    globals()['YTrainScaled'] = ScalerY.fit_transform(YTrain)
    globals()['XTestScaled'] = ScalerX.transform(XTest)
    globals()['YTestScaled'] = ScalerY.transform(YTest)

def Model(ModelType, FactorL1, FactorL2):
    def M():
        # Set seeds to avoid randomness
        seed(1)
        rd.set_seed(1)
        # Set parameters
        InputLength = len(DataColumns)-1
        Initializer = RandomUniform(minval = -0.01, maxval = 0.01, seed = 1)
        Activation = 'relu'
        if ModelType == 'Base':
            Regularizer = None
        elif ModelType == 'Lasso':
            Regularizer = regularizers.l1(FactorL1)
        elif ModelType == 'Ridge':
            Regularizer = regularizers.l2(FactorL2)
        elif ModelType == 'ElNet':
            Regularizer = regularizers.l1_l2(l1=FactorL1, l2=FactorL2)

        # Create architecture
        Model = Sequential()
        Model.add(Dense(32, 
                input_dim=InputLength, 
                kernel_initializer=Initializer, 
                activation=Activation,
                kernel_regularizer=Regularizer))
        Model.add(Dense(32, activation=Activation, kernel_initializer=Initializer))
        Model.add(Dense(8, activation=Activation, kernel_initializer=Initializer))
        Model.add(Dense(1, kernel_initializer=Initializer))
        # Compile model
        Model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
        return Model
    return M

def TrainModel(ModelType, FactorL1, FactorL2, Plot):
    # Define Wrapper
    Estimator = KerasRegressor(model=Model(ModelType, FactorL1, FactorL2), epochs=100, 
                                batch_size=5, verbose=0)
    # Cross validation
    kfold = KFold(n_splits=10)
    Results = cross_val_score(Estimator, XTrainScaled, YTrainScaled, cv=kfold, verbose=0,
                                scoring='neg_mean_squared_error')
    print("Cross Validation %a, L1 factor: %a, L2 factor: %a, MSE: %.4f (%.4f) " 
            % (ModelType, FactorL1, FactorL2, Results.mean(), Results.std()))
    # Fit model
    Estimator.fit(XTrainScaled, YTrainScaled, verbose=0)
    # Predict on the training data to see the fit
    YTrainPred = Estimator.predict(XTrainScaled)
    YTrainPred = ScalerY.inverse_transform(YTrainPred.reshape(-1, 1))
    # Mean Squared error on training prediction
    MSE_Train = mean_squared_error(YTrain, YTrainPred)
    print(("%a, L1 factor: %a, L2 factor: %a, MSE Train: %.4f" 
            % (ModelType, FactorL1, FactorL2, MSE_Train)))
    # Plot the training prediction to see the fit
    if Plot:
        if 'ax' in locals():
            plt.clf()
        fig, ax = plt.subplots()
        ax.plot(TrainDates, YTrain, label="YTrain")
        ax.legend()
        ax.plot(TrainDates, YTrainPred, label="YTrainPred")
        ax.legend()
        ax.set_title(ModelType, fontsize=12)
        ax.set_xlabel("Meses", fontsize=12)
        ax.set_ylabel("IPC", fontsize=12)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        plt.show()

    # Predict on the test data to evaluate the model
    YTestPred = Estimator.predict(XTestScaled)
    YTestPred = ScalerY.inverse_transform(YTestPred.reshape(-1, 1))
    # Mean Squared error on test prediction
    MSE_Test = mean_squared_error(YTest, YTestPred)
    # Coefficient of determination on test prediction
    R2 = Estimator.scorer(YTest, YTestPred)
    print(("%a, L1 factor: %a, L2 factor: %a, MSE Test: %.4f" 
            % (ModelType, FactorL1, FactorL2, MSE_Test)))
    # Consolidate the test evaluation metrics
    Models.append([("%a L1 factor: %a L2 factor: %a"
            % (ModelType, FactorL1, FactorL2)), Results.mean(), Results.std(), MSE_Test, R2])
    # Plot the test prediction to see the fit
    if Plot:
        fig, ax = plt.subplots()
        ax.plot(TestDates, YTest, label="YTest")
        ax.legend()
        ax.plot(TestDates, YTestPred, label="YTestPred")
        ax.legend()
        ax.set_title(ModelType, fontsize=12)
        ax.set_xlabel("Meses", fontsize=12)
        ax.set_ylabel("IPC", fontsize=12)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        plt.show()

def TrainSetModels(Whose, Plot):

    TrainModel('Base', None, None, Plot)
    if Whose == 'All':
        for i in range(-10,-1):
            TrainModel('Lasso', 10**i, None, Plot)
        for j in range(-10,-1):
            TrainModel('Ridge', None, 10**j, Plot)
        for i in range(-10,-1):
            for j in range(-10,-1):
                TrainModel('ElNet', 10**i, 10**j, Plot)
    elif Whose == 'Best':
        TrainModel('Lasso', 1e-3, None, Plot)
        TrainModel('Ridge', None, 1e-7, Plot)
        TrainModel('ElNet', 1e-3, 1e-5, Plot)
    
    for i in Models:
        print(i)

def run():
    DataImport()
    TrainSetModels('Best', False)
    
if __name__ == '__main__':
    run()
