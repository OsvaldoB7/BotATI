from datetime import datetime
from os import os 
from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

class bot_intra:
    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    
    def monitoramento(self):
        
        self.atualizando_pag = False
        navegador =self.driver
        while self.atualizando_pag == False:
            navegador.get('http://intranet.sefaz.to.gov.br/intranet/index-novo.asp')
            #path = abrindo.find_element_by_xpath('//*[@id="#home-conteudo"]/div[8]/div/div/div/table/tbody/tr[8]')
            sleep(5)
            navegador.refresh()