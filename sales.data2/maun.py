import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('all_Sales.csv') 
all_data = df
nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
#all_data['Month'] = all_data['Month'].astype('int32')

#print(all_data.head())
#print(nan_df.head())

temp_df = all_data[all_data['Order Date'].str[0:2] == 'Or']
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
# ===meek a month column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
# == meek a sales column = Quantity Ordered * Price Each']
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
results = all_data.groupby('Month').sum()
months = range(1,13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD($)')
plt.xlabel('Month number')
plt.show()