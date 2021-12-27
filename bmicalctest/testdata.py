# -*- coding: utf-8 -*-
"""
This file contains test parameters
Created on Sat Dec 25 11:11:07 2021
@author: Ramesh
"""


__inFileDir='bmicalctest/input/'
__outFileDir='bmicalctest/output/'

__inFileName='bmi_test.json'
__outFileName='bmiout_test'


inPath= __inFileDir+__inFileName
outPath= __outFileDir+__outFileName
colNames=['Gender', 'HeightCm', 'WeightKg','BMI','Category','HealthRisks']


outputFileFormat='CSV'
outputFileFormatList=['CSV','JSON']

countParam='Overweight' 


countParamBMHealthRisk={0:["Malnutrition risk",8],1:["Low risk",5],
           2:["Enhanced risk",7],3:["Medium risk",2],
           4:["High risk",2],5:["Very high risk",6]}

countParamBMICat={0:["Underweight",8],1:["Normal weight",5],
           2:["Overweight",7],3:["Moderately obese",2],
           4:["Severely obese",2],5:["Very severely obese",6]}


BMITable=[[0,18.5,'Underweight','Malnutrition risk'],
          [18.5,25,'Normal weight','Low risk'],
          [25,30,'Overweight','Enhanced risk'],
          [30,35,'Moderately obese','Medium risk'],
          [35,40,'Severely obese','High risk'],
          [40,100,'Very severely obese','Very high risk']]

