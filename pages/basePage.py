import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:

    def __init__(self):
        pass

    def getDriver(self):
        options = Options()
        options.add_argument("--start-fullscreen")
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=r"C:\HillRom\Automation\selenium-python\resources\chromedriver.exe")
        return self.driver

    def closeDriver(self):
        self.driver.close()
