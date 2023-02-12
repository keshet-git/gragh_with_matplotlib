
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
#use the '.uply()' to meek a city column

#op1 all_data['City'] =all_data['Purchase Address'].apply(lambda x: x.split(',')[1])
def get_city(addrress):
    return addrress.split(',')[1]


def get_state(addrress):
    return addrress.split(',')[2].split(' ')[1]

#all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} + ({get_state(x)})")

results = all_data.groupby('City').sum()
#print(results)
#cities = all_data['City'].unique()
cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation='vertical', size=8)
plt.ylabel('Sales in USD($)')
plt.xlabel('City name')
plt.show()

#print(all_data.head())