# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:59:10 2021
@author: Ramesh
"""

from bmicalctest import testdata
from src.bmicalc.bmicalc import bmicalculator


def test_bmiCatCount():
    bmicalobj=bmicalculator(testdata.BMITable)
    
    df=bmicalobj.loadData(testdata.inPath,testdata.colNames)
    df.loc[:, 'BMI'] = bmicalobj.calcBMI(df.loc[:,'WeightKg'], df.loc[:,'HeightCm']/100)
   
    df.loc[:, 'Category'] = df.loc[:,'BMI'].apply(lambda x: bmicalobj.getBMICategory(x))

    for key in testdata.countParamBMICat:        
        cnt=df['Category'].loc[df['Category']==testdata.countParamBMICat[key][0]].count()
        assert cnt ==testdata.countParamBMICat[key][1]
   

def test_bmiHealthRiskCount():
    bmicalobj=bmicalculator(testdata.BMITable)
    
    
    df=bmicalobj.loadData(testdata.inPath,testdata.colNames)
    df.loc[:, 'BMI'] = bmicalobj.calcBMI(df.loc[:,'WeightKg'], df.loc[:,'HeightCm']/100)
   
    df.loc[:, 'HealthRisks'] = df.loc[:,'BMI'].apply(lambda x: bmicalobj.getHealthRisks(x))

    for key in testdata.countParamBMHealthRisk:
        cnt=df['HealthRisks'].loc[df['HealthRisks']==testdata.countParamBMHealthRisk[key][0]].count()
        assert cnt ==testdata.countParamBMHealthRisk[key][1]



    
