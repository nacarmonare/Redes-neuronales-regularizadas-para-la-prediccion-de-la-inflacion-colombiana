# import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

variables = ['Inflación total']

#the PATH has to be in path
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

BanRepLink = 'https://totoro.banrep.gov.co/estadisticas-economicas/'
driver.get(BanRepLink)
# print(driver.title)

search = driver.find_element_by_id("formbuscador2:keyword")
search.send_keys(variables[0])
search.send_keys(Keys.RETURN)

# try:
WebDriverWait(driver, timeout = 10).until(
    EC.presence_of_element_located((By.ID, "form:dgresultados_data"))
)

results = driver.find_elements_by_xpath('//tr[@data-ri]//a')

# titles = []
# for result in results:
#     titles.append(result.text)

# print(titles)

results[0].click()


# WebDriverWait(driver, timeout = 10).until(EC.visibility_of_element_located((By.NAME, "svg")))

driver.find_element_by_xpath(
    '//*[name()="svg"]//*[@class="highcharts-exporting-group"]//*[@class="highcharts-button-symbol"]'
    ).click()
driver.find_element_by_xpath('//li[2]').click()


        # title = result.BanRepLink
# finally:
#     # driver.close() #close only the tab
#     driver.quit() #close the browser

#EC.presence_of_element_located((By.XPATH, '//tr[@data-ri="0"]//a'))

#maestría
# search = driver.find_element_by_xpath(xpath)


# print(driver.page_source)


# time.sleep(5)



CSVLink = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/BJsales.csv'
