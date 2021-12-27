# -*- coding: utf-8 -*-
"""
BMI utility processing class
Created on Fri Dec 24 16:16:55 2021
@author: Ramesh
"""

import pandas as pd
    
class bmicalculator():
    
    def __init__(self,table):
        self.BMITable = table
    
    def setTable(self,table):
        self.BMITable = table
        
        
    def loadData(self,filePath,cols):
            data=pd.read_json(filePath)
            data=pd.DataFrame(data,columns=cols)
            return data
    
    def getHealthRisks(self,bmi):
        #Assumed 0<bmi<=100
        retVal= 'Invalid data'
        if bmi>0 and bmi<=100:
            for r in self.BMITable:
                
                if bmi>=r[0] and bmi< r[1]:
                    retVal= r[3]
                    break
        return retVal
    def getBMICategory(self,bmi):
        #Assumed 0<bmi<=100
        retVal= 'Invalid data'
        if bmi>0 and bmi<=100:        
            for r in self.BMITable:   
                if bmi>=r[0] and bmi< r[1]:
                    retVal= r[2]
                    break
        return retVal
        
    def calcBMI(self,weight,hight):
        bmi=round((weight/hight**2),2)       
        return bmi
    
    def isValidHight(self,hight):
        retVal=True
        if not(hight>0 & hight<200):
            retVal=False
        return retVal
    
    def isValidWeight(self,weight):
        retVal=True
        if not (weight>0 & weight<200):
            retVal=False
        return retVal
            

