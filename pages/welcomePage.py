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

class WelcomePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.config = testConfig.MyConfig()
        self.upLoadTabXpath = r"//button[@id='ember21']"

    def waitUntilWelcomePageLoads(self):
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.upLoadTabXpath)))
            print("welcome Page Loaded!")
        except TimeoutException:
            print("unable to load welcome page due to timeout")


