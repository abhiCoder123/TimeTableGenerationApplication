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

time_table={}
classes_name=[]
for i in classes:
  classes_name.append((str((str(i).lstrip('[').rstrip(']'))).lstrip("'").rstrip("'")))
  time_table[(str((str(i).lstrip('[').rstrip(']'))).lstrip("'").rstrip("'"))]=df


#Useful Variables after Prcoessing the data
#classes_name : contains names of different years
#sorted_d : a dictionary containing subjects with their frequency in decreasing order
#time_table : containing time tables of different years
#subjects: contains map of different subjects with different years

new_dataset=dataset
new_dataset=new_dataset.drop(['Class'],axis=1)


#Algorithm to fill the time tables of respective years
count=0
subject_headers=list(new_dataset.columns.values)
slot_headers=list(df.columns.values)

slot_counters=[[0]*len(slot_headers)]*5

max_iter=0

import math
for key , value in sorted_d:
  temp_dict={}
  count=value
  while(count>0):
    print(1)
    for row in range(0,len(classes_name)):
      for column in range(0,len(subject_headers)):
        if(new_dataset.iloc[row,column]==key):
          curr_df=time_table[classes_name[row]]
          for period in range(0,len(slot_headers)):
            if(str(curr_df.iloc[0,period])=='nan'):
              if(period not in temp_dict and slot_counters[0][period]<=3):
                
               # curr_df.at[0:-1,period]=key
                #time_table[classes_name[row]].at[0:-1,period]=key
                temp_dict[period]=1
                print('much')
                for inc in range(0,4):
                  slot_counters[inc][period]=slot_counters[inc][period] + 1
                count=count-1
          
                
                