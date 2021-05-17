#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1 = ['p','p','e','s', 't', 'y']

list2 = ['e','e','s','s','t', 'y']

list3 = ['e','p','p','s', 't', 't']


import numpy as np
my_array = np.array([list1,
                    list2,
                    list3])

import pandas as pd
df = pd.DataFrame(my_array.T,
                   columns=['list1', 'list2', 'list3'])

list_of_max = []

for i in df.columns:
    if len(df[i].value_counts().loc[df[i].value_counts()== df[i].value_counts().max()]) >1:
        list_of_max.append('Много максимумов')
    else:   
        list_of_max.append(df[i].value_counts().idxmax()) #df[i].value_counts().max()])
    

    
print(list_of_max) 


# In[ ]:




