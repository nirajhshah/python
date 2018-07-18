# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:18:23 2016

@author: Niraj Shah
"""
from pandas.io.parsers import read_csv
class StateFarmAssignment:
    
       
    def cleanUpData(fileName):        
        data = read_csv(fileName)
        filtered_data = data.dropna(axis='rows', subset=['X1'], how='all')
        filtered_data = filtered_data.dropna(thresh=2)
        filtered_data = filtered_data.fillna(0)
        filtered_data.to_csv('CleanedData.csv')
        return filtered_data
    
    def buildLoadModel1():
        from StateFarmAssignment import cleanUpData    
        filtered_data = cleanUpData('OldData.csv')
        # Select training data. Columns (12:18,20:21) seem to have high p-values
       #dat = subset( filtered_data,select=c(2:17))
        
        # Fit the model
       # model = glm(Creditability~.,data=filtered_data,family=binomial)
        
        # Check the summary, variables equals to 0 do not count
       # summary(model)

    #def buildLoanModel2():
    #     cleanUpData('OldData.csv')
     from StateFarmAssignment import buildLoadModel1    
     buildLoadModel1()