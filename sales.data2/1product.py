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
temp_df = all_data[all_data['Order Date'].str[0:2] == 'Or']
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
# ===meek a month column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
# == meek a sales column = Quantity Ordered * Price Each']
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]


product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]

#plt.bar(products, quantity_ordered)
#plt.ylabel('Quantity Ordered')
#plt.xlabel('Product')
#plt.xticks(products, rotation='vertical', size=8)

#plt.show()
prices = all_data.groupby('Product').mean()['Price Each']
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel(('Product Name'))
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(products, rotation='vertical', size=8)

plt.show()
#print(prices)
'''
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

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

product_group = all_data.groupby('Product')

plt.bar(Product, quantity_ordered)
#print(product_group.sum())

#products = [product for product, df in product_group]

#plt.bar(products, quantity_ordered)
#plt.ylabel('Quantity Ordered')
#plt.xlabel('Product')
#plt.xticks(products, rotation='vertical', size=8)
#plt.show()

prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplot()

ax2 = ax1.twinx()
ax1.bar(products, Quantity_ordered)
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
plt.show()
#print(prices)
'''