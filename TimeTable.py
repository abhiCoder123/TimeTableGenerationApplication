#Importing the libraries
import pandas as pd
import numpy as np

#Importing the input as a csv file
dataset=pd.read_csv('input.csv')
classes=dataset.iloc[:, [0]].values
c=np.array(classes,dtype=str)
subjects=dataset.iloc[:,1:].values


#converting the input into suitable format
lis=[]
for item in subjects:
  lis.append((item))

#Preprocessing
number_of_classes=c.size
number_of_subjects=[]
for i in range (0,number_of_classes):
  number_of_subjects.append(lis[i].size)
  
lis1=[]
for item in lis:
  for it in item:
    lis1.append(str(it))

#Storing unique subjects    
set1=set(lis1)

new_dict={}

for i in set1:
  new_dict[i]=0
  
for i in lis1:
  new_dict[i]=new_dict[i] + 1
  

#sorted_d dictionary contains subjects sorted according to no. of classes  
import operator
sorted_d=sorted(new_dict.items(), key=operator.itemgetter(1),reverse=True)

df=pd.DataFrame(index=['Mon','Tue','Wed','Thu','Fri'],columns=['8-9','9-10','10-11','11-12','12-1','1-2','2-3','3-4','4-5'],dtype=str)

df.at[:,'12-1']='   Lunch Break   '


