from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


abrindo = webdriver.Chrome(executable_path=r'./chromedriver.exe')
abrindo.get('http://intranet.sefaz.to.gov.br/intranet/index-novo.asp')
if abrindo == True:
    abrindo.sleep(0.5)
    abrindo.refresh()
    print('Está atualizando')
else:
    print('Não atualizou')



