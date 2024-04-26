import os
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

import requests
from lxml import html
import time

from dotenv import load_dotenv

load_dotenv()
RUT = os.getenv('RUT_MPUENTES')
PASS = os.getenv('PASS_MPUENTES')


URL = "https://oficinajudicialvirtual.pjud.cl/home/"
path_driver ="/home/rduguet/Escritorio/proyectos_python/pjudScraping/drivers/"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(URL)

#ACTIONS
actions = ActionChains(driver=driver)


try:
    time.sleep(6)
    boton_1 = driver.find_element("xpath","/html/body/div[9]/div/section[1]/div/div[3]/div/div[1]/div/button").click()
    boton_1a = driver.find_element(By.XPATH, '/html/body/div[9]/div/section[1]/div/div[3]/div/div[1]/div/div/a[1]')
    time.sleep(5)
    
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
    
    #ingreso apartado causas
    mis_causas_button = driver.find_element(By.XPATH, '/html/body/div[1]/nav/ul/li[1]/a').click()
    
    #civil
    time.sleep(3)
    civil = driver.find_element(By.XPATH, '//*[@id="civilTab"]').click()
    
    #Principal 
    time.sleep(3)
    #evaluar hacer un ciclo FOR
    principal_activa = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/section/div/div/div[2]/div[3]/div/div/div[2]/div/div/table/tbody/tr[1]/td[1]/a/i').click()
    print(principal_activa)
    
    time.sleep(5)
except Exception as e :
    f"Error - {e}"
driver.close()