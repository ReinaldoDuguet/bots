import os
from selenium import webdriver 
from selenium.webdriver import ActionChains, FirefoxOptions

from bs4 import BeautifulSoup as bs
import csv

from lxml import html
import time
from datetime import datetime


URL = "https://www3.animeflv.net/"
options = FirefoxOptions()
options.add_argument('-headless')

driver = webdriver.Firefox(options=options)
driver.get(URL)

time.sleep(10)

def csvFunc(datos_header, datos_json):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    nombre = f'/csv/animes_actuales_{timestamp}.csv'

    with open(nombre, 'w',newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(datos_header)
        #writer.writerows(datos_json)
        writer.writerows([[dato] for dato in datos_json])

try:
    
    html = driver.page_source
    soup = bs(html, 'lxml')
    time.sleep(10)

    listado_animes = soup.find('div',{'class':'mCustomScrollBox mCS-light mCSB_vertical mCSB_inside'}).text.strip().split("\n")
    #print(listado_animes,len(listado_animes))
    
    datos_header = ["Nombre del Animé"]
    datos_json = []
    #lista_aCsv = []
    #for anime in listado_animes:
    #   lista_aCsv.append(anime)
    
    csvFunc(datos_header,listado_animes)

except Exception as e :
    f"Error - {e}"
driver.quit()