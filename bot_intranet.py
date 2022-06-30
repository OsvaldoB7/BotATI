from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime


horario_local = datetime.datetime.now()
print(horario_local)

atualizando_pag = False
abrindo = webdriver.Chrome(executable_path=r'./chromedriver.exe')
while atualizando_pag == False:
    abrindo.get('http://intranet.sefaz.to.gov.br/intranet/index-novo.asp')
    #path = abrindo.find_element_by_xpath('//*[@id="#home-conteudo"]/div[8]/div/div/div/table/tbody/tr[8]').text
    sleep(5)
    abrindo.refresh()

    
    
    
    
    




#abrindo.find_element_by_xpath('//*[@id="home-left"]/div[1]/a/img').click()




