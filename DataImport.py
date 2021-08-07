import pandas as pd
from selenium import webdriver

#the path has to be in PATH
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

BanRepLink = 'https://totoro.banrep.gov.co/estadisticas-economicas/'
driver.get(BanRepLink)


CSVLink = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/BJsales.csv'
