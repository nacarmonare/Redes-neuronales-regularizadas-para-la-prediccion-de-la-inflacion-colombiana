import os

import pandas as pd


def DataImport():
    #List of [FilesNames, DataFrameNames, Frequency]
    Variables = [['Inflación total', 'Inflaciontotal', ], 
    ['Tasa de política monetaria', 'TasaPoliticaMonetaria', ], 
    ['Tasa de desempleo', 'TasaDesempleo', ], 
    ['Tasa de ocupación', 'TasaOcupacion', ], 
    ['Consumo final, real', 'ConsumoFinaReal', ], 
    ['Producto Interno Bruto (PIB) real, Anual, base: 2015', 'PIB', ], 
    ['Índice de Precios del Productor (IPP)', 'IPP', ], 
    ['Meta de inflación', 'MetaInflacion', ], 
    ['Índice de Precios al Consumidor', 'IPC', ], 
    ['Tasa Representativa del Mercado (TRM)', 'TRM', ], 
    ['Base monetaria, mensual', 'BaseMonetaria', ], 
    ['Cuasidineros, total, mensual', 'CuasidinerosTotal', ], 
    ['Depósitos en el sistema financiero, total depósitos, mensual', 'DepositosSistemaFinanciero', ],
    ['M1, mensual', 'M1', ], 
    ['M2, mensual', 'M2', ], 
    ['M3, mensual', 'M3', ], 
    ['Reserva Bancaria, semanal', 'ReservaBancaria', ], 
    ['Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual', 'TotalCarteraBrutaTtitularizacionMonedaExtranjera', ], 
    ['Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual',  'TotalCarteraBrutaTtitularizacionMonedaLegal', ], 
    ['Crédito de consumo, Tasa de interés', 'CréditoConsumoTasaInteres', ], 
    ['Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual', 'DTF', ], 
    ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año', 'TasaInteresCeroCuponTES', ], 
    ['Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año', 'TasaInteresCeroCuponUVR', ], 
    ['Tasa de interés de colocación Banco de la República', 'TasaInteresColocacionBanRep', ], 
    ['Tasa interbancaria (TIB)', 'TIB', ], 
    ]

    FilesLocation = "Data\\"

    for Variable in Variables:
        globals()[Variable[1]] = pd.read_csv(os.path.join(FilesLocation, Variable[0].replace(":","") + ".csv"), 
                                        sep=';', 
                                        dtype={"Fecha": 'str', "Porcentaje (%)": 'float'}, 
                                        parse_dates=["Fecha"], 
                                        decimal=",")
        # exec("%s = %d" % (Variable[1], pd.read_csv(os.path.join(FilesLocation, Variable[0].replace(":","") + ".csv"), 
        #                                 sep = ';')))
                          
        print(globals()[Variable[1]].head())

def run():
    DataImport()


if __name__=="__main__":
    run()
