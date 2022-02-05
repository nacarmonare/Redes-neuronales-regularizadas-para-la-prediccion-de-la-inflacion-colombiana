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


def DescribeData():
    print(IPCTrain.describe())
    
    fig = plt.figure(figsize=(15, 15))
    ax = plt.subplot(1, 1, 1)
    ax.plot(IPCTrain)
    ax.set_title('IPCTrain')
    plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
    plt.show()

def FittingModel():
    ModelAuto2 = auto_arima(IPCTrain,m=12, max_order=None, alpha=0.05)
    print(ModelAuto2.summary())
    IPCTestPred = ModelAuto2.predict(n_periods=30)
    MSE_Test = mean_squared_error(IPCTest, IPCTestPred)
    print(MSE_Test)

    x = np.arange(150)
    plt.plot(x[:120], IPCTrain, c='blue', label="IPCTrain")
    plt.plot(x[120:], IPCTest, c='green', label="IPCTest")
    plt.plot(x[120:], IPCTestPred, c='red', label="IPCTestPred")
    plt.legend()
    plt.show()


def run():
    DataImport()
    FittingModel()

if __name__ == '__main__':
    run()
