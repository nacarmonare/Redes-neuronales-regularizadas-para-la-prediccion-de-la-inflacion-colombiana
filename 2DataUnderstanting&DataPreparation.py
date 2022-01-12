import os

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import StrMethodFormatter

FilesLocation = 'Data\\'
Variables = {
    'Inflaciontotal' : {
        'FilesName' : 'Inflación total',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'
    },
    'IPC' : {
        'FilesName' : 'Índice de Precios al Consumidor',
        'xLabel' : 'Meses',
        'yLabel' : 'Índice'
    },
    'TasaPoliticaMonetaria' : {
        'FilesName' : 'Tasa de política monetaria',
        'xLabel' : 'Días',
        'yLabel' : 'Porcentaje'        
    },
    'TasaDesempleo' : {
        'FilesName' : 'Tasa de desempleo',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'   
    },
    'TasaOcupacion' : {
        'FilesName' : 'Tasa de ocupación',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'   
    },
    'ConsumoFinalReal' : {
        'FilesName' : 'Consumo final, real',
        'xLabel' : 'Cuatrimestral',
        'yLabel' : 'Miles de millones COP'
    },
    'PIB' : {
        'FilesName' : 'Producto Interno Bruto (PIB) real, Anual, base: 2015',
        'xLabel' : 'Años',
        'yLabel' : 'Miles de millones COP'
    },
    'IPP' : {
        'FilesName' : 'Índice de Precios del Productor (IPP)',
        'xLabel' : 'Meses',
        'yLabel' : 'Índice'
    },
    'MetaInflacion' : {
        'FilesName' : 'Meta de inflación',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'
    },
    'TRM' : {
        'FilesName' : 'Tasa Representativa del Mercado (TRM)',
        'xLabel' : 'Días',
        'yLabel' : 'COP/USD'
    },
    'BaseMonetaria' : {
        'FilesName' : 'Base monetaria, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'CuasidinerosTotal' : {
        'FilesName' : 'Cuasidineros, total, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'DepositosSistemaFinanciero' : {
        'FilesName' : 'Depósitos en el sistema financiero, total depósitos, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'M1' : {
        'FilesName' : 'M1, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'M2' : {
        'FilesName' : 'M2, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'M3' : {
        'FilesName' : 'M3, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'ReservaBancaria' : {
        'FilesName' : 'Reserva Bancaria, semanal',
        'xLabel' : 'Semanal',
        'yLabel' : 'Miles de millones COP'
    },
    'TotalCarteraBrutaTitularizacionMonedaExtranjera' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'TotalCarteraBrutaTitularizacionMonedaLegal' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Miles de millones COP'
    },
    'CreditoConsumoTasaInteres' : {
        'FilesName' : 'Crédito de consumo, Tasa de interés',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'
    },
    'DTF' : {
        'FilesName' : 'Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'
    },
    'TasaInteresCeroCuponTES' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año',
        'xLabel' : 'Días hábiles',
        'yLabel' : 'Porcentaje'
    },
    'TasaInteresCeroCuponUVR' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año',
        'xLabel' : 'Días hábiles',
        'yLabel' : 'Porcentaje'
    },
    'TasaInteresColocacionBanRep' : {
        'FilesName' : 'Tasa de interés de colocación Banco de la República',
        'xLabel' : 'Meses',
        'yLabel' : 'Porcentaje'
    },
    'TIB' : {

        'FilesName' : 'Tasa interbancaria (TIB)',
        'xLabel' : 'Días hábiles',
        'yLabel' : 'Porcentaje'
    }
}

pd.set_option('float_format', '{:20,.2f}'.format)

def DataImport(): 
    for NameTimeSerie, DictTimeSerie in Variables.items():
        # Collect initial data
        DictTimeSerie['DataFrameOriginal'] = pd.read_csv(os.path.join(FilesLocation, DictTimeSerie['FilesName'].replace(':','') + '.csv'), 
                                                sep=';', 
                                                names=['Fecha', NameTimeSerie], 
                                                skiprows=1, 
                                                dtype={'Fecha': 'str', NameTimeSerie: 'float'}, 
                                                parse_dates=['Fecha'], 
                                                index_col=0, 
                                                decimal=',')

        # #Transforming Miles de Millones COP to Billones COP
        # if 'Miles de millones' in DictTimeSerie['DataFrameOriginal'].columns.values[0] :
        #     DictTimeSerie['DataFrameOriginal'] = DictTimeSerie['DataFrameOriginal'].div(1000)

        # DictTimeSerie['DataFrameOriginal'].columns = [NameTimeSerie]

        # Infer frequency
        if pd.infer_freq(DictTimeSerie['DataFrameOriginal'].index) == None :
            if NameTimeSerie == 'MetaInflacion':
                DictTimeSerie['Frequency'] = 'Need for filling'
            elif NameTimeSerie == 'ReservaBancaria':
                DictTimeSerie['Frequency'] = 'Not regular weekly frequency'
            elif NameTimeSerie == 'TasaInteresCeroCuponTES' or NameTimeSerie == 'TasaInteresCeroCuponUVR' or NameTimeSerie == 'TIB':
                DictTimeSerie['Frequency'] = 'Workdays'                 
        else:
            DictTimeSerie['Frequency'] = pd.infer_freq(DictTimeSerie['DataFrameOriginal'].index)
    # print(*Variables, sep='\n')

def DescribeData(BeforeFrequencyModification, ShowPlots):
    
    if ShowPlots: 
        fig = plt.figure(figsize=(15, 15))
    i = 1

    for NameTimeSerie, DictTimeSerie in Variables.items():
        if BeforeFrequencyModification:
            print(DictTimeSerie['DataFrameOriginal'].describe())
            if ShowPlots: 
                ax = plt.subplot(3, 3, i)
                ax.plot(DictTimeSerie['DataFrameOriginal'])
                ax.set_title(NameTimeSerie, fontsize=15)
                ax.set_xlabel(DictTimeSerie['xLabel'], fontsize=15)
                ax.set_ylabel(DictTimeSerie['yLabel'], fontsize=15)
                if DictTimeSerie['yLabel'] == 'Miles de millones COP':
                    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
                
                i += 1

                if i == 10 :
                    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)
                    plt.show()
                    i = 1

        else:

            if DictTimeSerie['Frequency'] != 'M':   #With frequency modification
                print(DictTimeSerie['DataFrameOriginal'].describe())
                print('After frequency modification')
                print(DictTimeSerie['DataFrameMonthly'].describe())
                if ShowPlots:
                    if 'ax' in locals():
                        plt.clf() #clean the plot
                    ax = plt.subplot(1, 2, 1)
                    ax.plot(DictTimeSerie['DataFrameOriginal'])
                    ax.set_title(NameTimeSerie, fontsize=15)
                    ax.set_xlabel(DictTimeSerie['xLabel'], fontsize=15)
                    ax.set_ylabel(DictTimeSerie['yLabel'], fontsize=15)
                    if DictTimeSerie['yLabel'] == 'Miles de millones COP':
                        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
                    
                    ax = plt.subplot(1, 2, 2)
                    ax.plot(DictTimeSerie['DataFrameMonthly'])
                    ax.set_title('Modificación: Promedio mensual ' + NameTimeSerie, fontsize=15)
                    ax.set_xlabel('Meses', fontsize=15)
                    ax.set_ylabel(DictTimeSerie['yLabel'], fontsize=15)
                    if DictTimeSerie['yLabel'] == 'Miles de millones COP':
                        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
                    plt.subplots_adjust(left=0.074,
                        bottom=0.4, 
                        right=0.98, 
                        top=0.952, 
                        wspace=0.21, 
                        hspace=0.4)
                    plt.show()
    
    if BeforeFrequencyModification and ShowPlots:
        plt.subplots_adjust(left=0.074,
            bottom=0.4, 
            right=0.98, 
            top=0.952, 
            wspace=0.21, 
            hspace=0.4)
        plt.show()
    
def VerifyDataQuality():
    for NameTimeSerie, DictTimeSerie in Variables.items():
        print(f"La variable {NameTimeSerie} contiene {DictTimeSerie['DataFrameOriginal'].isnull().sum().sum()} valores faltantes")

def FrequencyModification():
    MinDates = []
    MaxDates = []

    for NameTimeSerie, DictTimeSerie in Variables.items():

        if DictTimeSerie['Frequency'] != 'M':
            if DictTimeSerie['Frequency'] == 'D' or DictTimeSerie['Frequency'] == 'Not regular weekly frequency' or DictTimeSerie['Frequency'] == 'Workdays':
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].resample('M').mean()
                MinDates.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDates.append(DictTimeSerie['DataFrameMonthly'].index.max())
                print(f"La variable {NameTimeSerie} posee una frecuencia: {DictTimeSerie['Frequency']}")

            elif DictTimeSerie['Frequency'].find('Q') != -1 or DictTimeSerie['Frequency'].find('A') != -1 or DictTimeSerie['Frequency'] == 'Need for filling':
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].asfreq('M', method='ffill')
                MinDates.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDates.append(DictTimeSerie['DataFrameMonthly'].index.max())
                print(f"La variable {NameTimeSerie} posee una frecuencia: {DictTimeSerie['Frequency']}")

            else:
                print(DictTimeSerie['DataFrameOriginal'].tail(10))
        else:
            MinDates.append(DictTimeSerie['DataFrameOriginal'].index.min())
            MaxDates.append(DictTimeSerie['DataFrameOriginal'].index.max())

    globals()['MinDate'] = max(MinDates)
    globals()['MaxDate'] = min(MaxDates)

    print(f"La fecha más antigua que comparten todas las series de tiempo es {MinDate}, la fecha más reciente que comparten todas las series de tiempo es {MaxDate}")
    print(f"La fecha más antigua de todas las series de tiempo es {min(MinDates)}, la fecha más reciente de todas las series de tiempo es {max(MaxDates)}")

def DatasetCreation():
    i = 0

    for NameTimeSerie, DictTimeSerie in Variables.items():
        if DictTimeSerie['Frequency'] != 'M':   #With frequency modification
            # Serie between min date and max date
            DictTimeSerie['DataFrameMonthly'].rename(columns = {NameTimeSerie : 'Promedio mensual ' + NameTimeSerie}, inplace = True)
            SubSet = DictTimeSerie['DataFrameMonthly'][MinDate:MaxDate]
        else:
            # Serie between min date and max date
            SubSet = DictTimeSerie['DataFrameOriginal'][MinDate:MaxDate]

        i += 1

        # Final Dataset
        if i == 1:
            Dataset = SubSet
        else:
            Dataset = pd.merge_ordered(Dataset, SubSet, on='Fecha')

    print(Dataset)  

    #Shift the 'IPC' column back one, two and three months to create new predictive variables
    Dataset['IPC_1'] = Dataset['IPC'].shift(1)
    Dataset['IPC_2'] = Dataset['IPC'].shift(2)

    #Shift the 'IPC' column back one month to be the dependent variable
    Dataset['IPC_Y'] = Dataset['IPC'].shift(-1)
    Dataset = Dataset[2:-1]

    #Divde the datasets in train dataset and test dataset
    PercentageTrain = 0.8
    TrainDataSet = Dataset[: int(len(Dataset) * PercentageTrain)]
    TestDataSet = Dataset[int(len(Dataset) * PercentageTrain) :]

    # Save Original Datasets
    Dataset.to_csv(os.path.join(FilesLocation, 'Dataset.csv'), index=False)
    TrainDataSet.to_csv(os.path.join(FilesLocation, 'TrainDataSet.csv'), index=False)
    TestDataSet.to_csv(os.path.join(FilesLocation, 'TestDataSet.csv'), index=False)

def run():
    DataImport()
    DescribeData(BeforeFrequencyModification=True, ShowPlots=False)
    VerifyDataQuality()
    FrequencyModification()
    DescribeData(BeforeFrequencyModification=False, ShowPlots=False)
    DatasetCreation()

if __name__ == '__main__':
    run()
