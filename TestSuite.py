import TestSuiteRunner
import testConfig
import sys
import os
import time

def Tests():
    testModules = (
                     'SeleniumTestCase',           
                  )
    
    return testModules

def testRun_main():
    try:
        config = testConfig.MyConfig()
        sys.path.append(os.path.join(os.getcwd(), 'Testcases'))
        run = TestSuiteRunner.TestSuiteRunner()
        run.suite(Tests())
        
    except KeyboardInterrupt:
        print('test interupted')
    print("End Test")
    
if __name__ == '__main__':
    testRun_main()

