# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 17:54:35 2021

@author: Ramesh
"""

#import pytest
from bmicalctest import testdata
from src.bmicalc.bmicalc import bmicalculator

def test_getHealthRisks():
    bmicalobj=bmicalculator(testdata.BMITable)
        
    #if bmi<18.5:  HealthRisk= 'Malnutrition risk'
    assert bmicalobj.getHealthRisks(0) =='Invalid data'
    assert bmicalobj.getHealthRisks(15.9) =='Malnutrition risk'
    #if bmi>=18.5 and bmi<25: HealthRisk= 'Low risk'
    assert bmicalobj.getHealthRisks(22) =='Low risk'
    #if bmi>=25 and bmi<30: HealthRisk= 'Enhanced risk'
    assert bmicalobj.getHealthRisks(28.356) =='Enhanced risk'
    #if  bmi>=30 and bmi<35:  HealthRisk= 'Medium risk'
    assert bmicalobj.getHealthRisks(33) =='Medium risk'
    #if  bmi>=35 and bmi<40:  HealthRisk= 'High risk'
    assert bmicalobj.getHealthRisks(39.999) =='High risk'
    #if  bmi>=40: HealthRisk= 'Very high risk'
    assert bmicalobj.getHealthRisks(40) =='Very high risk'
        
def test_getBMICategory():
    bmicalobj=bmicalculator(testdata.BMITable)
        
    #if bmi<18.5: category= 'Underweight'
    assert bmicalobj.getBMICategory(0) =='Invalid data'
    assert bmicalobj.getBMICategory(15.9) =='Underweight'
    #if bmi>=18.5 and bmi<25: category= 'Normal weight'
    assert bmicalobj.getBMICategory(22) =='Normal weight'
    #if bmi>=25 and bmi<30: category= 'Overweight'
    assert bmicalobj.getBMICategory(28.356) =='Overweight'
    #if  bmi>=30 and bmi<35:  category= 'Moderately obese'
    assert bmicalobj.getBMICategory(33) =='Moderately obese'
    #if  bmi>=35 and bmi<40:  category= 'Severely obese'
    assert bmicalobj.getBMICategory(39.999) =='Severely obese'
    #if  bmi>=40: category= 'Very severely obese'
    assert bmicalobj.getBMICategory(40) =='Very severely obese'

def test_calcBMI():
    bmicalobj=bmicalculator(testdata.BMITable)
    
    weight=0.1
    hight=199        
    assert bmicalobj.calcBMI(weight,hight/100)==0.03
    weight=25.8
    hight=152        
    assert bmicalobj.calcBMI(weight,hight/100)==11.17
    
    weight=117.5
    hight=160        
    assert bmicalobj.calcBMI(weight,hight/100)==45.9
    
    weight=75
    hight=175        
    assert bmicalobj.calcBMI(weight,hight/100)==24.49

    
    
   
    
    