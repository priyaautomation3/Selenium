import os
import re
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from pages import basePage
from pages import mainPage

class HelperPage:
    """Some Documentation about the configuration"""
    
    def __init__(self):
        self.basePage = basePage.BasePage()

    def getDriver(self):
        self.driver = self.basePage.getDriver()
        return self.driver  

    def closeDriver(self):
        self.basePage.closeDriver()
        


        

    
