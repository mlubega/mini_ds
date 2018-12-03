# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Some usual imports here
import csv as csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

UNINSURED_DATA_FILE = 'the-number-of-estimated-eligible-uninsured-people-for-outreach-targeting.csv';
OUTPATIENT_DATA_FILE = '';
INPATIENT_DATA_FILE = '';

uninsured_data = pd.read_csv(UNINSURED_DATA_FILE);

# drop unneccesary columns
drop_from_uninsured = [ 'StateFIPS', 'PumaState', 'PUMA',
       'NoEnglishAdults_in_House', 'EnglishSpeaking', 'Spanish',
       'Chinese', 'Korean', 'Vietnamese', 'Tagalog', 'Russian', 'OtherLang',
       'SpeaksMostCommonOthLang', 'OtherLanguage']

uninsured_data.drop(drop_from_uninsured, inplace=True, axis=1);

# convert data to correct types 
int_cols = ['uninsured_total', 'Foodstamp', 'Age0_18', 'Age19_25', 'Age26_34', 'Age35_54', 'Age55_64', '138PctFPL_or_Less', '139to400PctFPL', 'Above400PctFPL', 'Male', 'Female', 'Married', 'ChildinFamily', 'Latino', 'WhiteNonLatino', 'BlackNonLatino', 'AsianNonLatino', 'HawaiiPacIslander', 'AmericanIndian_AlaskaNative', 'Multiracial_or_Other', 'Disabled', 'FullTime_Worker_in_Family', 'Job_Agriculture', 'Job_Mining', 'Job_ManufacturingConstruction', 'Job_Trade', 'Job_InfoFinance', 'Job_EducHealth', 'Job_Entertainment', 'Job_Service', 'Job_MilitaryPublic', 'LessThanHS', 'HSDiploma','CollegeGrad']
str_cols = ['StateName', 'Counties Within PUMA']
float_cols = ['uninsured_percent']

##  removes comma in numeric values
uninsured_data[int_cols] = uninsured_data[int_cols].apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',',''), errors='coerce'), axis=1);


#stats (mean, std, max, min, quartiles) of dataset
uninsured_stats = uninsured_data.describe()
print(uninsured_stats)




