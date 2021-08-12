# import pandas as pd
import time
import os
import shutil

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

variables = ['Inflación total'
            ,'Tasa de política monetaria'
            ,'Tasa de desempleo'
            ,'Tasa de ocupación'
            ,'Consumo final, real'
            ,'Producto Interno Bruto (PIB) real, Anual, base: 2015'
            ,'Índice de Precios del Productor (IPP)'
            ,'Meta de inflación'
            ,'Índice de Precios al Consumidor'
            ,'Tasa Representativa del Mercado (TRM)'
            ,'Base monetaria, mensual'
            ,'Cuasidineros, total, mensual'
            ,'Depósitos en el sistema financiero, total depósitos, mensual'
            ,'M1, mensual'
            ,'M2, mensual'
            ,'M3, mensual'
            ,'Reserva Bancaria, semanal'
            ,'Total Cartera Bruta sin ajuste por titularización en moneda extranjera , expresada en COP, mensual'
            ,'Total Cartera Bruta sin ajuste por titularización en moneda legal, mensual'
            ,'Crédito de consumo, Tasa de interés'
            ,'Tasa de Depósitos a Término Fijo (DTF) a 90 días, mensual'
            ,'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), pesos - 1 año'
            ,'Tasa de interés Cero Cupón, Títulos de Tesorería (TES), UVR - 1 año'
            ,'Tasa de interés de colocación Banco de la República'
            ,'Tasa interbancaria (TIB)']


#the PATH has to be in path
PATH = 'C:\Program Files (x86)\chromedriver.exe'

#Save files in the specified location
chrome_options = webdriver.ChromeOptions()
shutil.rmtree("Data\\" , True)
os.mkdir("Data\\")
FilesLocation = "C:\\Users\\natic\\TrabajoFinal\\Data\\"
prefs = {'download.default_directory' : FilesLocation}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options ,executable_path=PATH)

BanRepLink = 'https://totoro.banrep.gov.co/estadisticas-economicas/'

for variable in variables:
    
    #Open the link    
    driver.get(BanRepLink)
    # print(driver.title)

    try:
        #variable search
        search = driver.find_element_by_id("formbuscador1:autobuscador_input")
        search.send_keys(variable)
        time.sleep(3)

        results = driver.find_elements_by_xpath('//tr[@data-item-label = "' + variable + '"]')
        results[0].click()

        #download button
        WebDriverWait(driver, timeout = 20).until(
            EC.presence_of_element_located((By.XPATH, 
            '//*[name()="svg"]//*[@class="highcharts-exporting-group"]//*[@class="highcharts-button-symbol"]'))
        )

        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[name()="svg"]//*[@class="highcharts-exporting-group"]//*[@class="highcharts-button-symbol"]'
            ).click()
        driver.find_element_by_xpath('//li[2]').click()
        time.sleep(2)

        #rename cvs
        filename = os.path.join(FilesLocation, 'chart.csv') 
        shutil.move(filename,os.path.join(FilesLocation, variable.replace(":","") + ".csv"))

    except:
        print(f'La variable {variable} no fue descargada.')


#close the browser
driver.quit()