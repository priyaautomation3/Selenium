#!/usr/bin/env python

import time
import sys
import re
import os
import testConfig
import unittest


class TestSuiteRunner:

    def __init__(self):
        self.config = testConfig.MyConfig()
     
    def suite(self, modules):
        """This function takes a tuple of test case files(modules) as input and execute them
        """
        modules_to_test = modules
        try:
            for module in map(__import__, modules_to_test):
                tests = unittest.TestSuite()
                os.chdir(self.config.getProjectPath())              
                tests.addTest(unittest.findTestCases(module))
                testrunner=unittest.TextTestRunner()
                testrunner.run(tests)
                
        except KeyboardInterrupt:
            print('exception')
            
        return tests

def testRunner_main():
    try:
        x = TestSuiteRunner()

        while(True):
            time.sleep(2)
        
    except KeyboardInterrupt:
        print('*** Stopped by User ***')
    print("end test")
    
if __name__ == '__main__':
    testRunner_main()

