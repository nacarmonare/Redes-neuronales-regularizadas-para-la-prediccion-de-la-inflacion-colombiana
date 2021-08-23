import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

MinDates = []
MaxDates = []
FilesLocation = 'Data\\'
Variables = {
    'Inflaciontotal' : {
        'FilesName' : 'Inflación total'
    },
    'IPC' : {
        'FilesName' : 'Índice de Precios al Consumidor'
    },
    'TasaPoliticaMonetaria' : {
        'FilesName' : 'Tasa de política monetaria'
    },
    'TasaDesempleo' : {
        'FilesName' : 'Tasa de desempleo'
    },
    'TasaOcupacion' : {
        'FilesName' : 'Tasa de ocupación'
    },
    'ConsumoFinaReal' : {
        'FilesName' : 'Consumo final, real'
    },
    'PIB' : {
        'FilesName' : 'Producto Interno Bruto (PIB) real, Anual, base: 2015'
    },
    'IPP' : {
        'FilesName' : 'Índice de Precios del Productor (IPP)'
    },
    'MetaInflacion' : {
        'FilesName' : 'Meta de inflación'
    },
    'TRM' : {
        'FilesName' : 'Tasa Representativa del Mercado (TRM)'
    },
    'BaseMonetaria' : {
        'FilesName' : 'Base monetaria, mensual'
    },
    'CuasidinerosTotal' : {
        'FilesName' : 'Cuasidineros, total, mensual'
    },
    'DepositosSistemaFinanciero' : {
        'FilesName' : 'Depósitos en el sistema financiero, total depósitos, mensual'
    },
    'M1' : {
        'FilesName' : 'M1, mensual'
    },
    'M2' : {
        'FilesName' : 'M2, mensual'
    },
    'M3' : {
        'FilesName' : 'M3, mensual'
    },
    'ReservaBancaria' : {
        'FilesName' : 'Reserva Bancaria, semanal'
    },
    'TotalCarteraBrutaTitularizacionMonedaExtranjera' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual'
    },
    'TotalCarteraBrutaTitularizacionMonedaLegal' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual'
    },
    'CreditoConsumoTasaInteres' : {
        'FilesName' : 'Crédito de consumo, Tasa de interés'
    },
    'DTF' : {
        'FilesName' : 'Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual'
    },
    'TasaInteresCeroCuponTES' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año'
    },
    'TasaInteresCeroCuponUVR' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año'
    },
    'TasaInteresColocacionBanRep' : {
        'FilesName' : 'Tasa de interés de colocación Banco de la República'
    },
    'TIB' : {
        'FilesName' : 'Tasa interbancaria (TIB)'
    }
}

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

def DescribeData(BeforeFrequencyModification):
    fig = plt.figure(figsize=(15, 15))
    i = 1

    for NameTimeSerie, DictTimeSerie in Variables.items():
        if BeforeFrequencyModification:
            print(DictTimeSerie['DataFrameOriginal'].describe())
            ax = plt.subplot(3, 3, i)
            ax.plot(DictTimeSerie['DataFrameOriginal'])
            ax.set_title(NameTimeSerie)
            i += 1
        else:

            if DictTimeSerie['Frequency'] != 'M':   #With frequency modification
                print(DictTimeSerie['DataFrameOriginal'].describe())
                ax = plt.subplot(1, 2, 1)
                ax.plot(DictTimeSerie['DataFrameOriginal'])
                ax.set_title(NameTimeSerie)

                print('After frequency modification')
                print(DictTimeSerie['DataFrameMonthly'].describe())
                ax = plt.subplot(1, 2, 2)
                ax.plot(DictTimeSerie['DataFrameMonthly'])
                ax.set_title('After frequency modification')

                plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
                plt.show()

        if i == 10 and BeforeFrequencyModification:
            plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
            plt.show()
            i = 1
    
    if BeforeFrequencyModification:
        plt.subplots_adjust(left=0.1,
                bottom=0.1, 
                right=0.9, 
                top=0.9, 
                wspace=0.4, 
                hspace=0.4)
        plt.show()
    
def VerifyDataQuality():
    for NameTimeSerie, DictTimeSerie in Variables.items():
        print(f"La variable {NameTimeSerie} contiene {DictTimeSerie['DataFrameOriginal'].isnull().sum().sum()} valores faltantes")

def FrequencyModification():

    for NameTimeSerie, DictTimeSerie in Variables.items():

        if DictTimeSerie['Frequency'] != 'M':
            if DictTimeSerie['Frequency'] == 'D' or DictTimeSerie['Frequency'] == 'Not regular weekly frequency' or DictTimeSerie['Frequency'] == 'Workdays':
                #######################################PREGUNTAR
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].resample('M').mean()
                MinDates.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDates.append(DictTimeSerie['DataFrameMonthly'].index.max())
                print(f"La variable {NameTimeSerie} posee una frecuencia: {DictTimeSerie['Frequency']}")

            elif DictTimeSerie['Frequency'].find('Q') != -1 or DictTimeSerie['Frequency'].find('A') != -1 or DictTimeSerie['Frequency'] == 'Need for filling':
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].asfreq('M', method='ffill')
                MinDates.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDates.append(DictTimeSerie['DataFrameMonthly'].index.max())

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
            SubSet = DictTimeSerie['DataFrameMonthly'][MinDate:MaxDate]
        else:
            # Serie between min date and max date
            SubSet = DictTimeSerie['DataFrameOriginal'][MinDate:MaxDate]

        # Normalize
        ######################## PREGUNTAR normalización de variables TasaPolíticaMonetaria, PIB, MetaInflacion
        Scaler = MinMaxScaler(feature_range=(0, 1))
        DictTimeSerie['DataFrameFinal'] = pd.DataFrame(Scaler.fit_transform(SubSet),
                                                index=SubSet.index,
                                                columns=SubSet.columns)
        i += 1

        # Final Dataset
        if i == 1:
            globals()['Dataset'] = SubSet
            globals()['NormalizedDataset'] = DictTimeSerie['DataFrameFinal']
        else:
            globals()['Dataset'] = pd.merge_ordered(Dataset, SubSet, on='Fecha')
            globals()['NormalizedDataset'] = pd.merge_ordered(NormalizedDataset, DictTimeSerie['DataFrameFinal'], on='Fecha')

    print(Dataset)  
    print(NormalizedDataset)
    # Save Dataset
    Dataset.to_csv(os.path.join(FilesLocation, 'Dataset.csv'))
    NormalizedDataset.to_csv(os.path.join(FilesLocation, 'NormalizedDataset.csv'))

def run():
    DataImport()
    DescribeData(BeforeFrequencyModification=True)
    VerifyDataQuality()
    FrequencyModification()
    DescribeData(BeforeFrequencyModification=False)
    DatasetCreation()

if __name__ == '__main__':
    run()
