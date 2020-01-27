import pandas as pd
import numpy as np

# Read the data from a csv file
import plot as plot

us_babies = pd.read_csv('../Data/us_baby_names.csv')

#print(us_babies)

# // What were the 5 most popular baby names in 2014 in the U.S.?
# 1. Slice out the rows for 2014
us_babies['Year'] == 2014
us_babies_2014 = us_babies.loc[us_babies['Year'] == 2014, :]
# 2. Sort rows in descending order by count
sorted_us_2014 = us_babies_2014.sort_values('Count', ascending= False)

# 3. Get the first five rows
first_five_2014 = sorted_us_2014.iloc[0:5]
print('These are the 5 most popular names in the U.S. in 2014')
print(first_five_2014)

# Read the states info
states_babies = pd.read_csv('../Data/state_baby_names.csv')
#print(states_babies)

# // What were the 5 most popular baby names in 2014 in California?
# 1. Slice out the rows for 2014
states_babies_2014 = states_babies.loc[states_babies['Year'] == 2014, :]

# 2. Slice out the rows for California
states_babies_2014_Cali = states_babies_2014.loc[states_babies_2014['State'] == 'CA', :]

# 3. Sort rows in descending order by count
sorted_babies_2014_Cali = states_babies_2014_Cali.sort_values('Count', ascending= False)

# 4. get the first five rows
first_five_2014_Cali = sorted_babies_2014_Cali.iloc[0:5]
print('These are the 5 most popular names in California in 2014')
print(first_five_2014_Cali)

# // In California, what was the most populare female and male baby names for each year?
# 1. Slice out the rows for California
ca_babies = states_babies.loc[states_babies['State'] == 'CA', :]

# 2. Group resulting DataFrame by 'Year' and 'Gender
def popular(s):
    """Receives s, a Pandas Series, containing baby names in order of highest count to lowest count.
    Returns the most popular name in s."""
    return s.iloc[0]

# Above function are used to aggregate the result from the below statement, with the .agg() method
ca_grouped = ca_babies.sort_values('Count', ascending= False).groupby(['Year', 'Gender']).agg(popular)
print(ca_grouped)
# 3. Compute the most popular name for each group


# // How often does my first name occur across the years in the US among baby names?
# 1. find all the baby names that equals Rasmus
us_babies_Rasmus = us_babies.loc[us_babies['Name'] == 'Rasmus', :]

# 2. Create a horizontal bar plot to that displays the count of my first name over the years
plot = us_babies_Rasmus.plot.barh(x='Year', y='Count')
# Show the plot in the SciView in PyCharm
plot.figure.show()