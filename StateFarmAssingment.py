# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:18:23 2016
Data Model Exercise for StateFarm
@author: Niraj Shah
Great learning expereince and understanding power of python
Utilizing Spyder Python 3.5 Anaconda
pip install pandas and numphy and statsmodel
"""


import pandas as pd
import statsmodels.api as sm
import numpy as np
#setting up ignoring errors
np.seterr(divide='ignore', invalid='ignore')
#import read_csv
from pandas.io.parsers import read_csv
class StateFarmAssignment:
    
    #Step 1: cleanUpData method cleans the input csv file and returns the DataFrame
    def cleanUpData(fileName):     
        #utilizing pandas dataFrame and read csv file
        filteredData = read_csv(fileName, low_memory=False)      
        #drop data which has more than 2 column with bad data
        filteredData = filteredData.dropna(thresh=2)
        #filling up other values with 0 as it may be usefull
        filteredData = filteredData.fillna(0)
        #making all other data values to have numbers, removing % , etc
        filteredData['X1'].replace(regex=True,inplace=True,to_replace='%',value=r'')
        filteredData['X4'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
        filteredData['X5'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
        filteredData['X30'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
        #returning the DataFrame
        return filteredData
    
    #Step 2.a: building the first data model
    def buildLoadModel1(filteredData):
         #further clean down first column, as cleanupData method being used to clean test data as well
        filteredData = filteredData.dropna(axis='rows', subset=['X1'], how='all')
        #setting intercept
        filteredData['X1'] = 1
        #utilizing loan amount and salary
        X = filteredData[['X5','X13']]
        y = filteredData['X1']        
        
        #utilizing OLS, moretime might have helped figure out better model
        smresults = sm.OLS(y, X.astype(float)).fit()      
        #display out summary of model
        print(smresults.summary())
        return smresults
     
    #Step 2.b: building the second data model
    def buildLoadModel2(filteredData):
         #further clean down first column, as cleanupData method being used to clean test data as well
        filteredData = filteredData.dropna(axis='rows', subset=['X1'], how='all')
        filteredData['X1'] = 1
        X = filteredData[['X1','X2']]
        y = filteredData['X13']        
        #utilizing OLS, moretime might have helped figure out better model
        smresults = sm.OLS(y, X.astype(float)).fit() 
        #display out summary of model
        print(smresults.summary())
        return smresults
    
    #step 3: Testing supplied models and creating files for results
    def predictTestData(smresults, filteredData, columnName, multiplier, fileName):
        #predicting results based on model created
        filteredDataInterest =smresults.predict(pd.DataFrame({'X1': 1, 
                                          'X5': [filteredData[columnName].astype('float64')]})) * multiplier
        #get first column as interest column                           
        filteredData['X1']=filteredDataInterest[0]
        #round the data frame
        filteredData['X1']=filteredData['X1'].round(2)
        #convert to string and add %
        filteredData['X1'] = filteredData['X1'].astype(str) + '%'
        #save entire dataframe back as csv file for supplied names
        filteredData.to_csv(fileName)
   
  
filteredData = StateFarmAssignment.cleanUpData('Data for Cleaning & Modeling.csv')
smresultsModel1=StateFarmAssignment.buildLoadModel1(filteredData)
smresultsModel2=StateFarmAssignment.buildLoadModel2(filteredData)

testData = StateFarmAssignment.cleanUpData('Holdout for Testing.csv')
StateFarmAssignment.predictTestData(smresultsModel1,testData, 'X5', 100, "Results from Model1 Niraj Shah.csv")
StateFarmAssignment.predictTestData(smresultsModel2,testData, 'X13', 0.1, "Results from Model2 Niraj Shah.csv")