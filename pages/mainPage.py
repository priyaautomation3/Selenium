import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.join(os.getcwd(), '..'))
import testConfig

class MainPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.config = testConfig.MyConfig()
        self.homeUserButtonXpath = r"//a[contains(text(),'Dexcom CLARITY for Home Users')]"

    @property
    def homeUserButton(self):
        return self.driver.find_element_by_xpath(self.homeUserButtonXpath)

    def launchMainPage(self):
        self.driver.get(self.config.getApplicationUrl())
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.homeUserButtonXpath)))
            print("Main Page loaded!")
        except TimeoutException:
            print("Unable to load main page due to timeout")
        
    def clickDexcomCLARITYforHomeUsersButton(self):
        self.homeUserButton.click()

    def maximizeMainPage(self):
        self.driver.maximize_window()


