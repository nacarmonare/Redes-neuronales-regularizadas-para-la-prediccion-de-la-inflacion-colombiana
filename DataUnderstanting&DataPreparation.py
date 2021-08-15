import os

import matplotlib.pyplot as plt
import pandas as pd

Variables = {
    'Inflaciontotal' : {
        'FilesName' : 'Inflación total',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaPoliticaMonetaria' : {
        'FilesName' : 'Tasa de política monetaria',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaDesempleo' : {
        'FilesName' : 'Tasa de desempleo',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaOcupacion' : {
        'FilesName' : 'Tasa de ocupación',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'ConsumoFinaReal' : {
        'FilesName' : 'Consumo final, real',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'PIB' : {
        'FilesName' : 'Producto Interno Bruto (PIB) real, Anual, base: 2015',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'IPP' : {
        'FilesName' : 'Índice de Precios del Productor (IPP)',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'MetaInflacion' : {
        'FilesName' : 'Meta de inflación',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'IPC' : {
        'FilesName' : 'Índice de Precios al Consumidor',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TRM' : {
        'FilesName' : 'Tasa Representativa del Mercado (TRM)',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'BaseMonetaria' : {
        'FilesName' : 'Base monetaria, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'CuasidinerosTotal' : {
        'FilesName' : 'Cuasidineros, total, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'DepositosSistemaFinanciero' : {
        'FilesName' : 'Depósitos en el sistema financiero, total depósitos, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'M1' : {
        'FilesName' : 'M1, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'M2' : {
        'FilesName' : 'M2, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'M3' : {
        'FilesName' : 'M3, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'ReservaBancaria' : {
        'FilesName' : 'Reserva Bancaria, semanal',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TotalCarteraBrutaTitularizacionMonedaExtranjera' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TotalCarteraBrutaTitularizacionMonedaLegal' : {
        'FilesName' : 'Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'CreditoConsumoTasaInteres' : {
        'FilesName' : 'Crédito de consumo, Tasa de interés',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'DTF' : {
        'FilesName' : 'Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaInteresCeroCuponTES' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaInteresCeroCuponUVR' : {
        'FilesName' : 'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TasaInteresColocacionBanRep' : {
        'FilesName' : 'Tasa de interés de colocación Banco de la República',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    },
    'TIB' : {
        'FilesName' : 'Tasa interbancaria (TIB)',
        'DataFrameOriginal' : None,
        'Frequency' : None,
        'DataFrameMonthly' : None
    }
}

def DataImport():
    FilesLocation = 'Data\\'

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

    for NameTimeSerie, DictTimeSerie in Variables.items():
        if BeforeFrequencyModification:
            print(DictTimeSerie['DataFrameOriginal'].describe())
            plt.DictTimeSerie['DataFrameOriginal'].hist()
        else:
            if DictTimeSerie['Frequency'] != 'M':   #With frequency modification
                print(DictTimeSerie['DataFrameOriginal'].describe())
                DictTimeSerie['DataFrameOriginal'].hist()
                print('After frequency modification')
                print(DictTimeSerie['DataFrameMonthly'].describe())
                DictTimeSerie['DataFrameMonthly'].hist()

def VerifyDataQuality():
    for NameTimeSerie, DictTimeSerie in Variables.items():
        print(f"La variable {NameTimeSerie} contiene {DictTimeSerie['DataFrameOriginal'].isnull().sum().sum()} valores faltantes")

def FrequencyModification():
    MinDate = []
    MaxDate = []

    for NameTimeSerie, DictTimeSerie in Variables.items():

        if DictTimeSerie['Frequency'] != 'M':
            if DictTimeSerie['Frequency'] == 'D' or DictTimeSerie['Frequency'] == 'Not regular weekly frequency' or DictTimeSerie['Frequency'] == 'Workdays':
                ####################################################################### PREGUNTAR
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].resample('M').mean()
                MinDate.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDate.append(DictTimeSerie['DataFrameMonthly'].index.max())
                print(f"La variable {NameTimeSerie} posee una frecuencia: {DictTimeSerie['Frequency']}")

            elif DictTimeSerie['Frequency'].find('Q') != -1 or DictTimeSerie['Frequency'].find('A') != -1 or DictTimeSerie['Frequency'] == 'Need for filling':
                DictTimeSerie['DataFrameMonthly'] = DictTimeSerie['DataFrameOriginal'].asfreq('M', method='ffill')
                MinDate.append(DictTimeSerie['DataFrameMonthly'].index.min())
                MaxDate.append(DictTimeSerie['DataFrameMonthly'].index.max())

            else:
                print(DictTimeSerie['DataFrameOriginal'].tail(10))
        else:
            MinDate.append(DictTimeSerie['DataFrameOriginal'].index.min())
            MaxDate.append(DictTimeSerie['DataFrameOriginal'].index.max())
    
    print(f"La fecha más antigua que comparten todas las series de tiempo es {max(MinDate)}, la fecha más reciente que comparten todas las series de tiempo es {min(MaxDate)}")
    print(f"La fecha más antigua de todas las series de tiempo es {min(MinDate)}, la fecha más reciente de todas las series de tiempo es {max(MaxDate)}")

def run():
    DataImport()
    DescribeData(BeforeFrequencyModification=True)
    VerifyDataQuality()
    FrequencyModification()
    DescribeData(BeforeFrequencyModification=False)

if __name__ == '__main__':
    run()   


# # List of [FilesNames, DataFrameNames, DataFrameOriginal, Frequency, DataFrameMonthly]
# Variables = [['Inflación total', 'Inflaciontotal', ], 
#     ['Tasa de política monetaria', 'TasaPoliticaMonetaria', ], 
#     ['Tasa de desempleo', 'TasaDesempleo', ], 
#     ['Tasa de ocupación', 'TasaOcupacion', ], 
#     ['Consumo final, real', 'ConsumoFinaReal', ], 
#     ['Producto Interno Bruto (PIB) real, Anual, base: 2015', 'PIB', ], 
#     ['Índice de Precios del Productor (IPP)', 'IPP', ], 
#     ['Meta de inflación', 'MetaInflacion', ], 
#     ['Índice de Precios al Consumidor', 'IPC', ], 
#     ['Tasa Representativa del Mercado (TRM)', 'TRM', ], 
#     ['Base monetaria, mensual', 'BaseMonetaria', ], 
#     ['Cuasidineros, total, mensual', 'CuasidinerosTotal', ], 
#     ['Depósitos en el sistema financiero, total depósitos, mensual', 'DepositosSistemaFinanciero', ],
#     ['M1, mensual', 'M1', ], 
#     ['M2, mensual', 'M2', ], 
#     ['M3, mensual', 'M3', ], 
#     ['Reserva Bancaria, semanal', 'ReservaBancaria', ], 
#     ['Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual', 'TotalCarteraBrutaTtitularizacionMonedaExtranjera', ], 
#     ['Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual',  'TotalCarteraBrutaTtitularizacionMonedaLegal', ], 
#     ['Crédito de consumo, Tasa de interés', 'CreditoConsumoTasaInteres', ], 
#     ['Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual', 'DTF', ], 
#     ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año', 'TasaInteresCeroCuponTES', ], 
#     ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año', 'TasaInteresCeroCuponUVR', ], 
#     ['Tasa de interés de colocación Banco de la República', 'TasaInteresColocacionBanRep', ], 
#     ['Tasa interbancaria (TIB)', 'TIB', ], 
#     ]

# exec(f"{Variable[1]}= pd.read_csv(os.path.join(FilesLocation, NameTimeSerie.replace(':','') + '.csv'), sep=';')')
#  [['Inflación total', 'Inflaciontotal', 'M'], ['Tasa de política monetaria', 'TasaPoliticaMonetaria', 'D'], ['Tasa de desempleo', 'TasaDesempleo', 'M'], ['Tasa de ocupación', 'TasaOcupacion', 'M'], ['Consumo final, real', 'ConsumoFinaReal', 'Q-DEC'], ['Producto Interno Bruto (PIB) real, Anual, base: 
# 2015', 'PIB', 'A-DEC'], ['Índice de Precios del Productor (IPP)', 'IPP', 'M'], ['Meta de inflación', 'MetaInflacion', 'Mensual, Completar últimos meses'], ['Índice de Precios al Consumidor', 'IPC', 'M'], ['Tasa Representativa del Mercado (TRM)', 'TRM', 'D'], ['Base monetaria, mensual', 'BaseMonetaria', 'M'], ['Cuasidineros, total, mensual', 'CuasidinerosTotal', 'M'], ['Depósitos en el sistema financiero, total depósitos, mensual', 'DepositosSistemaFinanciero', 'M'], ['M1, mensual', 'M1', 'M'], ['M2, mensual', 'M2', 'M'], ['M3, mensual', 'M3', 'M'], ['Reserva Bancaria, semanal', 'ReservaBancaria', 'Semanal pero no pareja'], ['Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual', 'TotalCarteraBrutaTtitularizacionMonedaExtranjera', 'M'], ['Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual', 'TotalCarteraBrutaTtitularizacionMonedaLegal', 'M'], ['Crédito de consumo, Tasa de interés', 'CréditoConsumoTasaInteres', 'M'], ['Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual', 'DTF', 'M'], ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año', 'TasaInteresCeroCuponTES', 'Diario, hábiles'], ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año', 'TasaInteresCeroCuponUVR', 'Diario, hábiles'], ['Tasa de interés de colocación Banco de la República', 'TasaInteresColocacionBanRep', 'M'], ['Tasa interbancaria (TIB)', 'TIB', 'Diario, hábiles']]                                                    



        # Read the csv files
        # The headers are settled like 'Fecha', Name of the dataframe
        # globals()[Variable[1]] = pd.read_csv(os.path.join(FilesLocation, NameTimeSerie.replace(':','') + '.csv'), 
        #                                 sep=';', 
        #                                 names=['Fecha', Variable[1]], 
        #                                 skiprows=1, 
        #                                 dtype={'Fecha': 'str', Variable[1]: 'float'}, 
        #                                 parse_dates=['Fecha'], 
        #                                 index_col=0, 
        #                                 decimal=',')  


        # print(globals()[Variable[1]].tail())
        # print(pd.infer_freq(globals()[Variable[1]]['Fecha']))
        