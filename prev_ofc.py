import easygui
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


msg = "Cole os dados de login no formato:\n\n|CNPJ    |Senha   |\n|00000000|00000000|\n|00000000|00000000|"
title = "Login"
data_input = easygui.enterbox(msg, title)


data_list = [line.split('|') for line in data_input.strip().split('\n') if line.strip()]
df = pd.DataFrame(data_list[1:], columns=data_list[0])






total = len(df)


for n in range(total):
    cnpj = df.loc[n, 'CNPJ    ']
    senha = df.loc[n, 'Senha   ']
    qtd_cnpj = len(str(cnpj))
    
    if qtd_cnpj < 8:
        zero = str(0)
        cnpj = str(0) + str(cnpj)
    else:
        print("")

    
    url = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoenca.asp"

    driver = webdriver.Chrome()
    driver.get('https://www3.dataprev.gov.br/conadem/ConsultaAuxDoenca.asp')
    
    driver.find_element("name", "txtCNPJraiz").send_keys(str(cnpj))
    driver.find_element("name", "txtSenha").send_keys(str(senha))

    time.sleep(25)
    url2 = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoencaCNPJCEIraiz.asp"
    url3 = "https://www3.dataprev.gov.br/conadem/ConsultaAuxDoencaCNPJCEI.asp?txtCNPJCEI="

    rows = 1+len(driver.find_elements(By.XPATH, f"//*[@id='form1']/div/center/table/tbody/tr[2]/td"))
    
    qtd_row = 0
    table=driver.find_element(By.XPATH,"//*[@id='form1']")
    for tr in table.find_elements(By.TAG_NAME, "tr"):
        #print(tr.text)
        qtd_row_unic = len(driver.find_elements(By.TAG_NAME, "tr"))
        qtd_row + 1
        #print(qtd_row)
    a = int(1)
    qtd_row_unic - 2
    #print(qtd_row_unic)
    
    n = 2
    start = 2
    stop = qtd_row_unic
    #qtd_row = len(driver.find_elements(By.XPATH,"//*[@id='form1']"))
    qtd_row_unic - 2
    print(qtd_row_unic)
    
    #data_tabela = len(driver.find_elements(By.XPATH,f"//*[@id='form1']/div/center/table/tbody/tr/"))
    #distintos = len(pd.unique(data_tabela))
    
    #print(stop)

    x = 2
    for i in range(start, stop):

        cn = driver.find_element(By.XPATH,f"//*[@id='form1']/div/center/table/tbody/tr[{i}]/td[2]").get_attribute("textContent")
        
        driver.find_element(By.XPATH,f"//*[@id='form1']/div/center/table/tbody/tr[{i}]/td[2]").click()
        #print(i)
   
        driver.find_element("name","exportar").click()
        time.sleep(5)
        driver.find_element("name","voltar2").click()
        time.sleep(10)

        #x += 1
        #x = x + 1

        ns=""
print("Finish")
driver.quit
