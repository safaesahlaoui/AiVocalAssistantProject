import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By
class music():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='E:\Program Files\chromedriver\chromedriver.exe')

    def playMusic(self,query):
        self.query=query
        self.driver.get(url='https://www.youtube.com/results?search_query='+query)
        video=self.driver.find_element(By.XPATH,'//*[@id="video-title"]')
        video.click()

#assis= music()
#assis.playMusic('adele')
time.sleep(100)