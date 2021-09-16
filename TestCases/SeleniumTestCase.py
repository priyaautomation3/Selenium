
'''
Test class for all selenium tests
'''

import sys
import os
import time
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
import testConfig
from helperFunctions import helperPage
from pages import mainPage
from pages import loginPage
from pages import welcomePage


#-----------------------------------------------------------------#
#   Selenium Test
#-----------------------------------------------------------------#

class Test_Selenium(unittest.TestCase):
    """Test Case for Selenium"""
   
    def setUp(self):
        self.config = testConfig.MyConfig()
        self.userName = self.config.getUserName()
        self.password = self.config.getPassword()
        
    def tearDown(self):
        pass

    def test_LoginPage(self):
        '''Testing login page'''
        self.pageHelper = helperPage.HelperPage()
        self.driver = self.pageHelper.getDriver()
        self.mainPage = mainPage.MainPage(self.driver)
        self.loginPage = loginPage.LoginPage(self.driver)
        self.welcomePage = welcomePage.WelcomePage(self.driver)

        self.mainPage.launchMainPage()
        self.mainPage.maximizeMainPage()
        self.mainPage.clickDexcomCLARITYforHomeUsersButton()
        
        self.loginPage.waitUntilLoginPageLoads()
        self.loginPage.enterUserName(self.userName)
        self.loginPage.enterPassword(self.password)
        self.loginPage.clickLoginButton()
        self.welcomePage.waitUntilWelcomePageLoads()
        self.pageHelper.closeDriver()
                    
#-----------------------------------------------------------------#
#   Main fucntion to run the test script without test suite
#-----------------------------------------------------------------#

def test_main():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_Selenium))
    unittest.TextTestRunner(verbosity=2).run(suite)
                            
if __name__ == '__main__':
    test_main()

    

