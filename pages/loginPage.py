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

class LoginPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.config = testConfig.MyConfig()
        self.userNameTextBoxXpath = r"//input[@id='username']"
        self.passwordTextBoxXpath = r"//input[@id='password']"
        self.loginButtonXpath = r"//input[@type='submit']"        

    @property
    def userNameTextBox(self):
        return self.driver.find_element_by_xpath(self.userNameTextBoxXpath)

    @property
    def passwordTextBox(self):
        return self.driver.find_element_by_xpath(self.passwordTextBoxXpath)

    @property
    def loginButton(self):
        return self.driver.find_element_by_xpath(self.loginButtonXpath)

    def waitUntilLoginPageLoads(self):
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.userNameTextBoxXpath)))
            print("Login Page Loaded!")
        except TimeoutException:
            print("unable to load login page due to timeout")
        
    def enterUserName(self, userName):
        self.userNameTextBox.send_keys(userName)

    def enterPassword(self, password):
        self.passwordTextBox.send_keys(password)

    def clickLoginButton(self):
        self.loginButton.click()

