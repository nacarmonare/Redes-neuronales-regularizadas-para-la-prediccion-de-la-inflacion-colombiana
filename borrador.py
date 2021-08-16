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
        