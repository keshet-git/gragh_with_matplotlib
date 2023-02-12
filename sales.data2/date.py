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
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
#print(all_data.head())

all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
select_column = all_data['Minute']
#print(select_column)

hours = [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Nmber of Orders')
plt.grid()
plt.show()

#print(all_data.groupby(['Hour']).count())