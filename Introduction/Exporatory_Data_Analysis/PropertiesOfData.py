import pandas as pd
import xlrd

crime = pd.read_csv('../Data/crime_boston.csv')
offense = pd.read_excel('../Data/offense_codes_boston.xlsx')

# Granularity
'''crime = datasetA, offense = datasetB
    Data Set B has a coarser granularity than Data Set A'''

crime_incident_number = crime.groupby('INCIDENT_NUMBER').count()
print(crime_incident_number)


# Identify the scope
'''This Data Set tells alot about the crimes in Boston from June 15,2015 to August 17, 2019.
    If you need information about crime in NYC, this is not a Data Set for you.
    Therefor the scope is Crime in Boston'''

print(crime.head())

