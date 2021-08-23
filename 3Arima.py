import os

import matplotlib.pyplot as plt
import pandas as pd
from pmdarima.arima import auto_arima

MinDates = []
MaxDates = []
FilesLocation = 'Data\\'
FilesName = 'Índice de Precios al Consumidor'

def DataImport(): 
    # Collect initial data
    globals()['IPC'] = pd.read_csv(os.path.join(FilesLocation, FilesName + '.csv'), 
                                            sep=';', 
                                            names=['Fecha', 'IPC'], 
                                            skiprows=1, 
                                            dtype={'Fecha': 'str', 'IPC': 'float'}, 
                                            parse_dates=['Fecha'], 
                                            index_col=0, 
                                            decimal=',')

def DescribeData():
    print(IPC.describe())
    
    fig = plt.figure(figsize=(15, 15))
    ax = plt.subplot(1, 1, 1)
    ax.plot(IPC)
    ax.set_title('IPC')
    plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
    plt.show()

def FittingModel():
    # Splitting the Data
    Size = int(len(IPC) * 0.8)
    IPCTrain, IPCTest = IPC.iloc[:Size], IPC.iloc[Size:]
    ModelAuto1 = auto_arima(IPCTrain)
    print(ModelAuto1.summary())
    ModelAuto2 = auto_arima(IPCTrain, m=12, max_order=None, alpha=0.05)
    print(ModelAuto2.summary())

def Descompose():
    descomposition = sm.tsa.seasonal_decompose(IPC['IPC'], model='mul', period=12)
    descomposition.plot()
    # fig = plt.figure(figsize=(15, 15))
    # ax = plt.subplot(1, 1, 1)
    # ax.plot(descomposition)
    # ax.set_title('Descomposition')
    # plt.subplots_adjust(left=0.1,
    #         bottom=0.1, 
    #         right=0.9, 
    #         top=0.9, 
    #         wspace=0.4, 
    #         hspace=0.4)
    # plt.show()



def run():
    DataImport()
    DescribeData()
    # FittingModel()
    Descompose()

if __name__ == '__main__':
    run()
