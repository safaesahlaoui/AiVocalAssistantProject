from selenium import webdriver
import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
class infow():
    #driver =webdriver.Chrome()

    query=None
    def __init__(self):
        option = Options().add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(executable_path='E:\Program Files\chromedriver\chromedriver.exe')

    def get_info(self,query):
        self.query=query
        self.driver.get(url='https://www.wikipedia.org')

        search= self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        time.sleep(100)# just make my navigator wait , probably it works without it test it first

#info= infow()
#info.get_info('Maroc')


