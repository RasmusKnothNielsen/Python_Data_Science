import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# Load the AirBnB Data Set
listings = pd.read_csv('../Data/AB_NYC_2019.csv')


# Create a histogram to display the distribution of the quantitative data in price column
plt.hist(listings['price'])
plt.xlabel('price (in US dollars)')
plt.show()

# Since the above histogram is hard to read, we need to reduce the spread in price.
plt.hist(listings['price'], bins=np.arange(0, 1100, 40))
plt.xlabel('price (in US dollars)')
plt.show()

# Scatterplotthat compares the prices of listings and number of reviews for those listings
plt.scatter(x= listings['price'], y=listings['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.show()

# Now, let's try to restrict the x axis, so the scatterplot only goes up to 1100
plt.scatter(x=listings['price'], y=listings['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0,1100)
plt.show()

# Suppose I want to decrease the size of the points on the scatter plot:
plt.scatter(x=listings['price'], y=listings['number_of_reviews'], s=5)
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0,1100)
plt.show()

'''From the above plots, we can see that there is a trend between the price of a listing
    and the total amount of reviews. 
    Is there an assotiation between the price and the number of reviews of listings?'''