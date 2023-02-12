import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('all_Sales.csv') 
all_data = df
nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')

df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df =df[['Order ID', 'Grouped']].drop_duplicates()
select_column = df['Grouped']
#print(select_column)

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]

plt.bar(products, quantity_ordered)
plt.xticks(products, rotation='vertical', size=8)
plt.show()