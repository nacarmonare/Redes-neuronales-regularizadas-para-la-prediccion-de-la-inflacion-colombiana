import os
import shutil
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def DataDownload():
    Variables = ['Inflación total', 
        'Tasa de política monetaria', 
        'Tasa de desempleo', 
        'Tasa de ocupación', 
        'Consumo final, real', 
        'Producto Interno Bruto (PIB) real, Anual, base: 2015', 
        'Índice de Precios del Productor (IPP)', 
        'Meta de inflación', 
        'Índice de Precios al Consumidor', 
        'Tasa Representativa del Mercado (TRM)', 
        'Base monetaria, mensual', 
        'Cuasidineros, total, mensual', 
        'Depósitos en el sistema financiero, total depósitos, mensual', 
        'M1, mensual', 
        'M2, mensual', 
        'M3, mensual', 
        'Reserva Bancaria, semanal', 
        'Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual', 
        'Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual', 
        'Crédito de consumo, Tasa de interés', 
        'Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual', 
        'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año', 
        'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año', 
        'Tasa de interés de colocación Banco de la República', 
        'Tasa interbancaria (TIB)', 
        ]

    #Delete the directory
    shutil.rmtree("Data\\", True)
    os.mkdir("Data\\")

    #Save files in the specified location
    ChromeOptions = webdriver.ChromeOptions()
    FilesLocation = "C:\\Users\\natic\\TrabajoFinal\\Data\\"
    prefs = {'download.default_directory': FilesLocation}
    ChromeOptions.add_experimental_option('prefs', prefs)
    Path = 'C:\Program Files (x86)\chromeDriver.exe'         # The Path has to be in path
    Driver = webdriver.Chrome(options = ChromeOptions, executable_path = Path)
    BanRepLink = 'https://totoro.banrep.gov.co/estadisticas-economicas/'

    for Variable in Variables:
        # Open the link    
        Driver.get(BanRepLink)
        #print(Driver.title)
        try:
            # Variable Search
            Search = Driver.find_element_by_id("formbuscador1:autobuscador_input")
            Search.send_keys(Variable)
            time.sleep(1)

            WebDriverWait(Driver, timeout = 10).until(
                EC.element_to_be_clickable((By.XPATH,
                '//tr[@data-item-label = "' + Variable + '"]'))
            )
            Results = Driver.find_elements_by_xpath('//tr[@data-item-label = "' + Variable + '"]')
            Results[0].click()
            time.sleep(1)
            
            # Download button
            WebDriverWait(Driver, timeout = 20).until(
                EC.presence_of_element_located((By.XPATH,
                '//*[name()="svg"]//*[@class="highcharts-exporting-group"]//*[@class="highcharts-button-symbol"]'))
            )
            Driver.find_element_by_xpath(
                '//*[name()="svg"]//*[@class="highcharts-exporting-group"]//*[@class="highcharts-button-symbol"]'
                ).click()
            Driver.find_element_by_xpath('//li[2]').click()
            time.sleep(3)

            # Rename cvs
            Filename = os.path.join(FilesLocation, 'chart.csv')
            shutil.move(Filename,os.path.join(FilesLocation, Variable.replace(":","") + ".csv"))

        except Exception as e:
            print(f'La Variable {Variable} no fue descargada. Error: {e}')

    # Close the browser
    Driver.quit()

def run():
    DataDownload()

if __name__=="__main__":
    run()
