
"""

This Module contains the configuration class for all tests. 
And also the path to the different files used in the test cases.

"""
import os
import re

class MyConfig:
    """Some Documentation about the configuration"""
    
    def __init__(self):
        pass    

    def getApplicationUrl(self):
        """Get App URL"""
        self.url = r"https://clarity.dexcom.com/"
        return self.url

    def getUserName(self):
        """Get App URL"""
        self.userName = r"codechallenge"
        return self.userName

    def getPassword(self):
        """Get App URL"""
        self.password = r"Password123"
        return self.password

    def getProjectPath(self):
        """"Project Path folder used by Genesis framework"""
        path = os.path.dirname(__file__)
        reg = re.compile('\\\\\w*\\\\[.][.]')
        path = reg.split(path)
        if not len(path) == 1:
            path[0] = path[0]+path[1]            
        return path[0]


        

    
