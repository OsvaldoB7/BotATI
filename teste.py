from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


abrindo = webdriver.Chrome(executable_path=r'./chromedriver.exe')
abrindo.get('http://intranet.sefaz.to.gov.br/intranet/index-novo.asp')
abrindo.find_element_by_xpath('//*[@id="home-left"]/div[1]/a/img').click()



