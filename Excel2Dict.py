# -*- coding: utf-8 -*-
###############################################
"""
Jays @ 8 Nov 2021
"""
###############################################

import pandas as pd
London = pd.read_csv("London_Text_Frequency.csv", header=0)
London.set_index(['Text'], inplace=True)
London.insert(2,'Weight_Alter','NaN')

Mel = pd.read_csv("Melbourne_Text_Frequency.csv", header=0)
Mel.set_index(['Text'], inplace=True)
Mel.insert(2,'Weight_Alter','NaN')


BNE = pd.read_csv("BNE_Text_Frequency.csv", header=0)
BNE.set_index(['Text'], inplace=True)
BNE.insert(2,'Weight_Alter','NaN')

##print (London)
##print (Mel)

##print (London.Text)
##print (Mel.Text)
##print (BNE.Text)


###############################################
London_Dict = London.to_dict (orient='index')
Mel_Dict = Mel.to_dict (orient='index')
BNE_Dict = BNE.to_dict (orient='index')
#############################################



"""
Match every street name of Mel  to that of London
"""


for key, value in Mel_Dict.items():
    
    
    ### Mel street names are included in that of London
    if key in London.index.tolist():
        
        Weight_London = London.at[key,'Weight']
            
        Weight_Alter = (value["Weight"] - Weight_London)/Weight_London
        
        #print (key,': ',Weight_Alter)
                
        
    ### Mel street names are not included in that of London
    else: 
        Weight_Alter = 'NaN'
        
        #print (key,':',Weight_Alter)
        
    Mel.at[key,'Weight_Alter'] = Weight_Alter


"""
Match every street name of BNE to that of London
"""

for key, value in BNE_Dict.items():
    
    
    ### BNE street names are included in that of London
    if key in London.index.tolist():
        
        Weight_London = London.at[key,'Weight']
            
        Weight_Alter = (value["Weight"] - Weight_London)/Weight_London
        
        #print (key,': ',Weight_Alter)
                
        
    ### BNE street names are not included in that of London
    else: 
        Weight_Alter = 'NaN'
       
        #print (key,':',Weight_Alter)
        
    BNE.at[key,'Weight_Alter'] = Weight_Alter
 
    
"""
Output new csv with "Weight Alter"
"""
BNE.to_csv ('BNE_new.csv')
Mel.to_csv ('Mel_new.csv')
    

