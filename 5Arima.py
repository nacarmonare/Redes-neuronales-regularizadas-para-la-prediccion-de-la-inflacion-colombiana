import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error

FilesLocation = 'Data\\'
FilesName = 'Índice de Precios al Consumidor'

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

    globals()['IPCTrain'] = TrainData.filter(['IPC_0']) 
    globals()['IPCTest'] = TestData.filter(['IPC_0']) 
    globals()['TrainDates'] = globals()['TrainData'].index.tolist()
    globals()['TestDates'] = globals()['TestData'].index.tolist()

def FittingModel():
    ModelAuto = auto_arima(IPCTrain,m=12, max_order=None, alpha=0.05)
    print(ModelAuto.summary())
    IPCTestPred = ModelAuto.predict(n_periods=30)
    MSE_Test = mean_squared_error(IPCTest, IPCTestPred)
    print(MSE_Test)

    x = np.arange(150)
    # plt.plot(TrainDates, IPCTrain, c='blue', label="IPCTrain")
    plt.plot(TestDates, IPCTest, c='green', label="IPCTest")
    plt.plot(TestDates, IPCTestPred, c='red', label="IPCTestPred")
    plt.legend()
    plt.grid()
    plt.show()


def run():
    DataImport()
    FittingModel()

if __name__ == '__main__':
    run()
