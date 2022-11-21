#pip install webdriver-manager
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.get('https://bra.ifsp.edu.br/servidores')


lista  = driver.find_element(By.XPATH, '//*[@id="content-section"]/div/div[1]/ul')
linhas  = lista.find_elements(By.TAG_NAME, "li")

for l in linhas:
  print(l.text)