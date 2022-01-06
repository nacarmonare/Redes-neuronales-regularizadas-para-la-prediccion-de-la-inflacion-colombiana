import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pygam import LinearGAM
from sklearn.preprocessing import MinMaxScaler

FilesLocation = 'Data\\'
FilesName = 'TrainDataSet'

def DataImport(): 
    # Collect initial data
    globals()['Data'] = pd.read_csv(os.path.join(FilesLocation, FilesName + '.csv'), 
                                            sep=',',
                                            parse_dates=['Fecha'], 
                                            index_col=0, 
                                            decimal='.')
    

    globals()['XData'] = Data.drop(['IPC','Inflaciontotal'], axis=1)
    globals()['YData'] = Data.filter(['IPC'])

    #Scale
    Scaler = MinMaxScaler(feature_range=(0, 1))
    globals()['XDataNormalized'] = pd.DataFrame(Scaler.fit_transform(XData),
                                                index = XData.index,
                                                columns = XData.columns)
    globals()['YDataNormalized'] = pd.DataFrame(Scaler.fit_transform(YData),
                                                index = YData.index,
                                                columns = YData.columns)

def Model():
    lams = np.logspace(-3, 3, 30)
    n_splines = np.arange(10)
    globals()['ModelGAM'] = LinearGAM().gridsearch(XDataNormalized.values, YDataNormalized.values, lam= lams, n_splines= n_splines)
    ModelGAM.summary()
    
    # titles = Data.drop(['IPC','Inflaciontotal','Fecha'], axis=1).columns
    titles = XData.columns
    fig = plt.figure(figsize=(15, 15))
    j = 0

    for i in range(0,23):
        XX = ModelGAM.generate_X_grid(term=i)
        ax = plt.subplot(2,4, j+1)
        ax.plot(XX[:, i], ModelGAM.partial_dependence(term=i, X=XX))
        ax.plot(XX[:, i], ModelGAM.partial_dependence(term=i, X=XX, width=.95)[1], c='r', ls='--')
        ax.set_title(titles[i])
        # ax.set_xlabel(DictTimeSerie['xLabel'])
        # plt.ylim(-0.12, 0.12)
        ax.set_ylabel('Impacto Marginal sobre el IPC')

        j += 1

        if i == 7 or i ==15:
            plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
            plt.show()
            j = 0

    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
    plt.show()

def run():
    DataImport()
    Model()

if __name__ == '__main__':
    run()
