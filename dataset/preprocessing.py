import pandas as pd
import numpy as np

# preprocessing dataset, making sure data is categorical and is suitable for the use by the KAD

lprice = pd.read_csv('laptop_price_original.csv')

# remove part of the attributes to make data more simple and categorical
lprice = lprice.drop('Product', axis=1)
lprice = lprice.drop('CPU_Type', axis=1)
lprice = lprice.drop('GPU_Type', axis=1)
lprice = lprice.drop('OpSys', axis=1)
lprice = lprice.drop('Weight (kg)', axis=1)

# removing extreme cases
lprice = lprice[lprice['Price (Euro)']<3000]

# define bins and labels for categorization
bins = [10, 12, 14, 16, 20]  # Define bin edges
labels = ['10-12', '12-14', '14-16', '16-20']  # Labels for bins

# assign categories for inches
lprice['Inches'] = pd.cut(lprice['Inches'], bins=bins, labels=labels)


# define bins and labels for categorization
bins = [0.8, 1.6, 2.4, 3.0, 4.0]  # Define bin edges
labels = ['0.8-1.6', '1.6-2.4', '2.4-3.0', '3.0-4.0']  # Labels for bins

# assign categories for cpu frequency
lprice['CPU_Frequency (GHz)'] = pd.cut(lprice['CPU_Frequency (GHz)'], bins=bins, labels=labels)


# define bins and labels for categorization
bins = [2, 4, 8, 16, 64]  # Define bin edges
labels = ['2-4', '4-8', '8-16', '16-64']  # Labels for bins

# assign categories for RAM
lprice['RAM (GB)'] = pd.cut(lprice['RAM (GB)'], bins=bins, labels=labels)


# define bins and labels for categorization
bins = [0, 700, 1400, 2100, 3000]  # Define bin edges
labels = ['0-700', '700-1400', '1400-2100', '2100-3000']  # Labels for bins

# assign categories for price
lprice['Price (Euro)'] = pd.cut(lprice['Price (Euro)'], bins=bins, labels=labels)

lprice_sample = lprice.sample(n=300)
print(len(lprice_sample))
lprice_sample.to_csv('lprice_sample.csv')