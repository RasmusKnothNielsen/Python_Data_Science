import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# Load the AirBnB Data Set
listings = pd.read_csv('../Data/AB_NYC_2019.csv')

# Now let's try to make a barchart of AirBnB listings in each neighbourhood group of NYC
sn.countplot(x='neighbourhood_group', data=listings)
plt.show()

# Another barchart that shows the average price of listings in each neighbourhood group
sn.barplot(x='neighbourhood_group', y='price', data=listings)
plt.show()

# The above chart has confidence intervals in it.
# What if we want to make a chart without confidence intervals?
sn.barplot(x='neighbourhood_group', y='price', data=listings, ci =False)
plt.show()