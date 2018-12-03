X# -*- coding: utf-8 -*-
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
INPATIENT_DATA_FILE_2015 = 'Medicare_Provider_Charge_Inpatient_DRGALL_FY2015.csv';
INPATIENT_DATA_FILE_2014 = 'Medicare_Provider_Charge_Inpatient_DRGALL_FY2014.csv';

charges_2015 = pd.read_csv(INPATIENT_DATA_FILE_2015);
charges_2015 = charges_2015.sample(frac=0.1);
mn_charges_2015 = charges_2015[charges_2015['Provider State'] == 'MN'];
charges_2015['Year'] = 2015;
charges_2015_grpd = charges_2015.groupby(['DRG Definition']).agg({ 'Total Discharges':'sum', 'Average Covered Charges': 'mean', 'Average Total Payments':'mean','Average Medicare Payments': 'mean' })


charges_2014 = pd.read_csv(INPATIENT_DATA_FILE_2014);
charges_2014 = charges_2014.sample(frac=0.1);
mn_charges_2014 = charges_2014[charges_2014['Provider State'] == 'MN'];
charges_2014['Year'] = 2014;
charges_2014_grpd = charges_2014.groupby(['DRG Definition']).agg({ 'Total Discharges':'sum', 'Average Covered Charges': 'mean', 'Average Total Payments':'mean','Average Medicare Payments': 'mean' })

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