#!/usr/bin/python
import numpy as np 
import pandas as pd 


titanic=pd.read_csv('titanic_data.csv') 
titanic=titanic[['Sex','Survived']]
print(titanic.head())
num_rows=float(titanic.shape[0])
p_survived = (titanic.Survived == 1).sum() / num_rows
p_unsurvived=1-p_survived
p_male=(titanic.Sex=='male').sum()/num_rows
p_female=1-p_male

num_women=titanic[titanic.Sex=='female'].shape[0]
women_who_survived=titanic[(titanic.Sex=='female') & (titanic.Survived==1)].shape[0]
p_survived_women=women_who_survived/float(num_women)

print("p(Surived|Female)=P(Survived and Female)/P(Female) is %f\n"%p_survived_women)
