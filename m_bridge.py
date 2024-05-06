import os
from selenium import webdriver
from bs4 import BeautifulSoup as bs 
from selenium.webdriver import ActionChains, Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait 

#import requests
#from lxml import html
import time
from dotenv import load_dotenv

load_dotenv()
RUT = os.getenv('RUT_MPUENTES')
PASS = os.getenv('PASS_MPUENTES')


URL = "https://oficinajudicialvirtual.pjud.cl/home/"

#enabling the background mode
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.page_load_strategy = 'none'
#driver = webdriver.Firefox(options=options)
driver = Firefox(options=options)
driver.implicitly_wait(3)

#driver = webdriver.Firefox()
#driver.maximize_window()
driver.get(URL)

#ACTIONS
actions = ActionChains(driver=driver)


try:
    time.sleep(6)
    boton_1 = driver.find_element("xpath","/html/body/div[9]/div/section[1]/div/div[3]/div/div[1]/div/button").click()
    boton_1a = driver.find_element(By.XPATH, '/html/body/div[9]/div/section[1]/div/div[3]/div/div[1]/div/div/a[1]')
    time.sleep(5)
    
    #posar mouse/cursor encima
    actions.move_to_element(boton_1a).perform()
    boton_1a.click()
    time.sleep(3)
    
    #LOGGING
    campo_rut = driver.find_element(By.XPATH, '//*[@id="uname"]')
    campo_rut.send_keys(RUT)
    
    campo_password = driver.find_element(By.XPATH, '//*[@id="pword"]')
    campo_password.send_keys(PASS)
    
    ingresar_button = driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()
    #FIN LOGGING
    
    # ingreso apartado causas
    mis_causas_button = driver.find_element(By.XPATH, '/html/body/div[1]/nav/ul/li[1]/a').click()
    
    # ingreso apartado civil
    time.sleep(5)
    civil = driver.find_element(By.XPATH, '//*[@id="civilTab"]').click()

    time.sleep(7)

    html = driver.page_source
    soup = bs(html,'lxml')
    time.sleep(5)

    #causas = soup.find('tbody',{'id':'verDetalleMisCauCiv'}).text
    causas = soup.find('table',{'id':"dtaTableDetalleMisCauCiv"}).text.strip()
    
    rit_causa = 'C-163-2021'
    estado_causa = 'Tramitación'
    cuaderno = 'Principal'

    if (estado_causa and cuaderno)  in causas:
        print(f"el rit de la causa es: {rit_causa} y esta en la posicion {causas.index(rit_causa)}")
        time.sleep(3)
        boton_causa = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/section/div/div/div[2]/div[3]/div/div/div[2]/div/div/table/tbody/tr[2]/td[1]/a/i').click()
        time.sleep(3)

        tabla_causa = soup.find('div',{'class':'anel panel-default'})
        print(f"la info de la causa es: {tabla_causa}")
        try:
            if '104':
                print("el ultimo estado de la causa es 104")
        except:
            print("no se encontró el ultimo estado de la causa o bien se cayó esta wea")

    else:
        print("lo siento, algo pasó en el proceso y no pude encontrar el elemento o BIEN LA CAUSA NO SE ENCUENTRA")
    #principal_activa = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/section/div/div/div[2]/div[3]/div/div/div[2]/div/div/table/tbody/tr[1]/td[1]/a/i').click()
    
    time.sleep(7)


except Exception as e :
    f"Error - {e}"
driver.close()
#driver.quit()