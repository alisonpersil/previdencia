import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
#mport urllib.request
import urllib.request, urllib.parse, urllib.error 
import pandas as pd
import urllib.parse
#import util
from urllib.request import urlopen
import re
import time
import numpy as np
#from sklearn.datasets import load_iris
from selenium.webdriver.common.by import By
import lxml.html as LH
import string





url = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoenca.asp"


driver = webdriver.Chrome()
driver.get('https://www3.dataprev.gov.br/conadem/ConsultaAuxDoenca.asp')
#driver.find_element("name", "txtCNPJCEI").send_keys("07955536000100")
#07955536 senha 81827364


driver.find_element("name", "txtCNPJraiz").send_keys("07955536")
driver.find_element("name", "txtSenha").send_keys("81827364")

time.sleep(25)
#html_read = resposta.read()
url2 = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoencaCNPJCEIraiz.asp"

url3 = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoencaCNPJCEI.asp?txtCNPJCEI="

rows = 1+len(driver.find_elements(By.XPATH, f"//*[@id='form1']/div/center/table/tbody/tr[2]/td"))
cn = driver.find_element(By.XPATH,f"//*[@id='form1']/div/center/table/tbody/tr[2]/td[2]").get_attribute("textContent")
a = int(1)

n = 2


start = 2
stop = rows + 2

print(rows)
x = 2
for i in range(start, stop):


    driver.find_element(By.XPATH,f"//*[@id='form1']/div/center/table/tbody/tr[{i}]/td[2]").click()
    print(i)
   
    driver.find_element("name","exportar").click()
    time.sleep(5)
    driver.find_element("name","voltar2").click()
    time.sleep(10)

    #x += 1
    #x = x + 1

    ns=""
driver.quit
