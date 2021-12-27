# -*- coding: utf-8 -*-
"""
Main BMI processing class
Created on Fri Dec 24 10:45:10 2021
@author: Ramesh
"""


from src.bmicalc import bmicalc
import os

class mainBMIApp():
      
    def __init__(self,dobj):
               
        self.__inPath= dobj["inFileDir"]+dobj["inFileName"]
        self.__outPath= dobj["outFileDir"]+dobj["outFileName"]
        self.__inFileDir=dobj["inFileDir"]
        self.__outFileDir=dobj["outFileDir"]
        self.__inFileName =dobj["inFileName"]
        self.__outFileName =dobj["outFileName"]        
        self.__colNames =dobj["colNames"].split(',')
        self.__outputFileFormat =dobj["outputFileFormat"]
        self.__countParam =dobj["countParam"]
        self.BMITable=[[0,18.5,'Underweight','Malnutrition risk'],
          [18.5,25,'Normal weight','Low risk'],
          [25,30,'Overweight','Enhanced risk'],
          [30,35,'Moderately obese','Medium risk'],
          [35,40,'Severely obese','High risk'],
          [40,100,'Very severely obese','Very high risk']]
         
        
    def __checkPara(self):
        projDir=os.getcwd()
        
        # Check whether the specified path is an existing directory or not 
        if not os.path.isdir(self.__inFileDir):
            raise IsADirectoryError(self.__inFileDir+": dir does not exixt in project directory "+projDir)
        else:
            if not os.path.os.path.exists(self.__inPath):
                 raise FileNotFoundError(self.__inPath+": File does not exixt in directory "+projDir)
        if not os.path.isdir(self.__outFileDir):
            path = os.path.join(projDir, self.__outFileDir)
            os.mkdir(path)
            
    def __loadDataFile(self,obj):
        #Load Data from input directory
        return obj.loadData(self.__inPath,self.__colNames)
    
    def __printData(self, df):
        
        #Print Data (JSON/CSV format) output dir
        if self.__outputFileFormat=='JSON':
            #Prind Data to JSON Format in Output Directory
            with open(self.__outPath+'.json', 'w') as f:
                f.write(df.to_json(orient='records'))
            f.close()        
        elif self.__outputFileFormat=='CSV':
            #Prind Data to CSV Format in Output Directory
            df.to_csv(self.__outPath+'.csv', mode='w', header=True, index=False)

    def __printCont(self,df):
        
        #Print at console Count the total number of overweight people 
        print(self.__countParam, ' count: ',  df['Category'].loc[df['Category']==self.__countParam].count())


    def processBMIData(self):
       
        self.__checkPara()
        
        obj=bmicalc.bmicalculator(self.BMITable)
        
        df= self.__loadDataFile(obj)
        #remove rows which are outside of range: Height and WeightKg
        df.where(df['HeightCm'] > 1, inplace = True)
        df.where(df['WeightKg'] > 0, inplace = True)
        #Calculate BMI
        df.loc[:, 'BMI'] = obj.calcBMI(df.loc[:,'WeightKg'], df.loc[:,'HeightCm']/100)
        #Asign BMI Category using Table 1 based on BMI
        df.loc[:, 'Category'] = df.loc[:,'BMI'].apply(lambda x: obj.getBMICategory(x))
        
        #Asign BMI HealthRisks using Table 1 based on BMI
        df.loc[:, 'HealthRisks'] = df.loc[:,'BMI'].apply(lambda x: obj.getHealthRisks(x))
        
        self.__printData(df)
        
        self.__printCont(df)
        