from selenium import webdriver
from multiprocessing.pool import ThreadPool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nome_produto = 'rtx 3060'
links = ['https://www.pichau.com.br/placa-de-video-msi-geforce-rtx-3060-ti-ventus-x2-oc-8gb-gddr6x-256-bit-912-v505-084',
         'https://www.pichau.com.br/placa-de-video-galax-geforce-rtx-3060-ti-1-click-oc-plus-8gb-gddr6x-256-bit-36ism6md2kcv',
         'https://www.pichau.com.br/placa-de-video-galax-geforce-rtx-3060-ti-1-click-oc-plus-8gb-gddr6x-256-bit-36ism6md2kcv-nac']
def acessar_pagina(link:str):
    driver = webdriver.Firefox()

    driver.get(link)
    nome = driver.find_elements(By.CSS_SELECTOR,'div.jss210')

    for nome_produto in nome:
        print(nome_produto.text)

    preco = driver.find_elements(By.CSS_SELECTOR, 'div.jss265')

    for valor in preco:
        print(valor.text)

    time.sleep(2)
    driver.close()
    return

# pool = ThreadPool(processes=12)
# threads = []

for link_placa in links:
    print('Vou procurar',link_placa)
    acessar_pagina(link_placa)
    # async_result = pool.map_async(acessar_pagina, (link_placa,))
    # threads.append(async_result)

while True:
    True