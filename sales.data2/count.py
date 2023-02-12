from itertools import combinations
from collections import Counter
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
count = Counter()

for row in df['Grouped']:
    row_list= row.split(',')
    count.update(Counter(combinations(row_list, 3)))

for key, value in count.most_common(10):
    print(key, value)
#print(count.most_common(10))