from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import getpass

def enterMarcacoes():
   load_dotenv()

   login = input("Digite seu login do EasyMOB\n")
   senha = getpass.getpass("Digite sua senha do EasyMOB\n")
   # login = os.getenv('login')
   # senha = os.getenv('senha')
   empresa = os.getenv('empresa')

   driver = webdriver.Chrome()
   driver.get("https://easymob.metadados.com.br/Account/LoginColaborador")

   driver.find_element(By.ID, "chave").send_keys(empresa)
   driver.find_element(By.ID, "usuario").send_keys(login)
   driver.find_element(By.ID, "senha").send_keys(senha)
   driver.find_element(By.ID, "btnLogin").click()

   WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btnConsultar"))).click()
   return driver

def getLastMonth():
   driver = enterMarcacoes()
   dias = [{
      "dia": "",
      "horarios": []
   }]

   rows = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//td")))
   for i, r in enumerate(rows):

      if "/" in rows[i].text and (rows[i].text != dias[-1]["dia"]):
         dias.append({
               "dia": rows[i].text,
               "horarios": [rows[i+1].text.split(":")[0] + ":" + rows[i+1].text.split(":")[1]]
            })
      if ":" in rows[i].text:
         hora = rows[i].text.split(":")[0] + ":" + rows[i].text.split(":")[1]
         if rows[i-1].text == dias[-1]["dia"] and hora != dias[-1]["horarios"][-1]:
            dias[-1]["horarios"].append(hora)

   dias.pop(0)
   for d in dias:
      print(d)

   driver.quit()

def getToday():
   driver = enterMarcacoes()
   dia = datetime.now().strftime("%d/%m/%Y")
   hojeElements = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, f"//tr/td[contains(text(), '{dia}')]/..")))

   horarios = []
   for he in hojeElements:
      horarios.append(he.find_element(By.XPATH, "./td[contains(text(), ':')]").text)

   horarios.sort()

   print("Hoje você bateu o ponto às: ")
   for h in horarios:
      print("-> " + h)

   driver.quit()
   # return horarios
