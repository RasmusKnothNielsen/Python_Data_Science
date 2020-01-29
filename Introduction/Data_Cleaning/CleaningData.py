import pandas as pd

crime = pd.read_csv('../Data/crime_boston.csv')

# Access rows that contain a null
print(crime.isnull().any(axis=1))

# Extract the indices of the rows with null values
# and use them to get the rows and save them as result
rows_with_missing_values = crime.isnull().any(axis=1)
result = crime[rows_with_missing_values]

# These are the rows with NaN values in them.
print(result)

# Now lets try to drop the year, month and hour columns
# since the occurred on date column already includes both date and time
cleaned_crime = crime.drop(columns=['YEAR', 'MONTH', 'HOUR'])

# Now lets check the DataFrame for misspellings.
# Let's start with 'OFFENSE_CODE_GROUP
print(cleaned_crime['OFFENSE_CODE_GROUP'].unique())
# THere seem to be no misspellings here.

# Now we are checking 'OFFENSE_DESCRIPTION
print(cleaned_crime['OFFENSE_DESCRIPTION'].unique())
# No misspellings seems to be present

# Now we check 'DAY_OF_WEEK'
print(cleaned_crime['DAY_OF_WEEK'].unique())
# No misspellings here.

# Now let'd frop the location column from the Data Set,
# since we already have this information in our Lat and Long columns.
cleaned_crime = cleaned_crime.drop(columns='Location')
print(cleaned_crime)