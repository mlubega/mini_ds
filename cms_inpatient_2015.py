# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Some usual imports here
import csv as csv 
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

UNINSURED_DATA_FILE = 'the-number-of-estimated-eligible-uninsured-people-for-outreach-targeting.csv';
OUTPATIENT_DATA_FILE = '';
INPATIENT_DATA_FILE_2015 = 'Medicare_Provider_Charge_Inpatient_DRGALL_FY2015.csv';
INPATIENT_DATA_FILE_2014 = 'Medicare_Provider_Charge_Inpatient_DRGALL_FY2014.csv';
not_needed = ['Provider Street Address', 'Hospital Referral Region (HRR) Description', 'Provider Name']

charges_2015 = pd.read_csv(INPATIENT_DATA_FILE_2015);
charges_2015 = charges_2015.drop(not_needed, axis=1);


charges_2014 = pd.read_csv(INPATIENT_DATA_FILE_2014);
charges_2014 = charges_2014.drop(not_needed, axis=1);


charges = pd.merge(charges_2014, charges_2015, on=['Provider Id', 'DRG Definition', 'Provider State', 'Provider Zip Code', 'Provider City'], suffixes=[2014, 2015])
## fix issues like this----
## 003 - ECMO OR TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.
## 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.

# total 
charges_grpd = charges.groupby(['DRG Definition']).agg({'Total Discharges2014':'sum',
                              'Average Covered Charges2014': 'mean',
                              'Average Total Payments2014':'mean',
                              'Average Medicare Payments2014': 'mean',
                              'Total Discharges2015':'sum',
                              'Average Covered Charges2015': 'mean',
                              'Average Total Payments2015':'mean',
                              'Average Medicare Payments2015': 'mean'});


plt.bar(charges_grpd.index, charges_grpd['Average Covered Charges2014'], align='center', alpha=0.5)
plt.bar(charges_grpd.index, charges_grpd['Average Covered Charges2015'], align='center', alpha=0.5)
plt.show


features = charges.iloc[:,5:11];
target = charges.iloc[:, 12];

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2);

lm = linear_model.LinearRegression();

model = lm.fit(x_train, y_train);
predictions = lm.predict(x_test);
model.score(x_test, y_test);

plt.scatter(y_test, predictions);
plt.xlabel('Actual Values');
plt.ylabel('Predictions');

#charges_2015_grpd = charges_2015.groupby(['DRG Definition']).agg({ 'Total Discharges':'sum', 'Average Covered Charges': 'mean', 'Average Total Payments':'mean','Average Medicare Payments': 'mean' })
#charges_2014_grpd = charges_2014.groupby(['DRG Definition']).agg({ 'Total Discharges':'sum', 'Average Covered Charges': 'mean', 'Average Total Payments':'mean','Average Medicare Payments': 'mean' })


#plt.bar(charges_2014_grpd.index, charges_2014_grpd['Average Covered Charges'], align='center', alpha=0.5)
#plt.bar(charges_2015_grpd.index, charges_2015_grpd['Average Covered Charges'], align='center', alpha=0.5)
#plt.show()
#charges = pd.concat([charges_2014, charges_2015])


#charges = pd.merge(charges_2015, charges_2014, on='DRG Definition', how='inner');

#EDA
#inpatient_charges.columns
#inpatient_charges.describe()
#
#treatments = inpatient_charges.groupby(['DRG Definition']).groups.keys()
#charges_grouped = inpatient_charges.groupby(['DRG Definition']).agg({ 'Total Discharges':'mean', 'Average Covered Charges': 'mean', 'Average Total Payments':'mean','Average Medicare Payments': 'mean' })
#
##charges_grouped.columns
#plt.bar(charges_grouped.index, charges_grouped['Average Covered Charges'], align='center')
#plt.bar(charges_grouped.index, charges_grouped['Average Total Payments'], align='center')
#plt.show()
#
#az_charges = inpatient_charges[inpatient_charges['Provider State'] == 'AZ']
#az_charges_grpd = az_charges.groupby(['DRG Definition']).agg({ 'Total Discharges':'sum', 'Average Covered Charges': 'sum', 'Average Total Payments':'sum','Average Medicare Payments': 'sum' })
#
# np.corrcoef(az_charges_grpd['Average Covered Charges'], az_charges_grpd['Average Total Payments'])
# plt.scatter(az_charges_grpd['Average Covered Charges'], az_charges_grpd['Average Total Payments'])
 
 #array([[1.        , 0.98922079], [0.98922079, 1.        ]])