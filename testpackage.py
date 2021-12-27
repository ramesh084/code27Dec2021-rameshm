# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:55:19 2021

@author: Ramesh
"""
import json
from src.bmicalc import mainapp
import datetime
import pytest
import os
if __name__ == '__main__':
    
    a = datetime.datetime.now()
         
    try:
        
        with open('parameters.json','r') as json_file:
            para = json.load(json_file)
        
        #Test package
        retcode = pytest.main()                   
        print(retcode)
        
        #following two lines used to Run package
        driverapp=mainapp.mainBMIApp(para)                
        driverapp.processBMIData()
        
        #following command can be used to  build package
        '''
        cmd='python -m build'
        retcode =os.system(cmd)        
        print(retcode)
        '''
    except Exception as e :
        print(e)
    
    b = datetime.datetime.now()
    c = b - a
    print(c.microseconds)